from flask import Flask, request, jsonify
import random
import docker
from consistent_hash import ConsistentHash

#Initialize the flask application
app = Flask(__name__)

#Initialize the Consistent Hashing Instance
ch = ConsistentHash()

#Initialize docker client
client = docker.from_env()

#List to keep track of server instances
servers = []

#Endpoint to get the current number of replicas and their hostnames
@app.route('/rep', methods=['GET'])
def get_replicas():
    return jsonify({
        "N": len(servers),
        "replicas": servers
    })

#Endpoint to add new server instances
@app.route('/add', methods=['POST'])
def add_servers():
    data = request.get_json() #Get JSON data from the request
    n = data.get('n') #Number of servers to add
    hostnames = data.get('hostnames', []) #Optional list of hostnames
    
    #Check if the number of provided hostnames exceeds the number of instances to add
    if len(hostnames) > n:
        return jsonify({"error": "Number of hostnames exceeds the number of instances to add"}), 400

    new_servers = []
    for i in range(n):
        #Generate a hostname if not provided
        hostname = hostnames[i] if i < len(
            hostnames) else f"server-{random.randint(1000, 9999)}"
        new_servers.append(hostname)
        
        #Start new Docker container with the given hostnames
        container = client.containers.run(
            "my_web_server_image",
            name=hostname,
            detach=True,
            environment={"SERVER_ID": hostname.split('-')[-1]}
        )
        
        #Add the server to the list and consistent hash ring
        servers.append(hostname)
        ch.add_server(hostname)

    return jsonify({
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    })

#Endpoint to remove server instances
@app.route('/rm', methods=['DELETE'])
def remove_servers():
    data = request.get_json() #Get JSON data from the requesy
    n = data.get('n') #Number of servers to remove
    hostnames = data.get('hostnames', []) #Optional list of hostnames
    
    #Check if the number of provided hostnames exceeds the number of instances to remove
    if len(hostnames) > n:
        return jsonify({"error": "Number of hostnames exceeds the number of instances to remove"}), 400

    to_remove = []
    if hostnames:
        for hostname in hostnames:
            if hostname in servers:
                to_remove.append(hostname)
            else:
                return jsonify({"error": f"Hostname {hostname} not found"}), 400
    else:
        to_remove = random.sample(servers, n) #Randomly select servers to remove if no hostnames provided

    for hostname in to_remove:
        #Stop and remove the Docker container
        container = client.containers.get(hostname)
        container.stop()
        container.remove()
        #Remove the server from the list and consistent hash ring
        servers.remove(hostname)
        ch.remove_server(hostname)

    return jsonify({
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    })

#Endpoint to route incoming requests to the appropriate server based on consistent hashing
@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    server = ch.get_server(path) #Get the server for the given path
    if server:
        #Execute a command in the Docker container to get the response for the given path
        container = client.containers.get(server)
        response = container.exec_run(f"curl -s http://localhost:5000/{path}")
        return response.output.decode('utf-8')
    else:
        return "No servers available", 500

#Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

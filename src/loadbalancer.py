from flask import Flask, request, jsonify
import random
import docker
from consistent_hash import ConsistentHash

app = Flask(__name__)
ch = ConsistentHash()
client = docker.from_env()

servers = []


@app.route('/rep', methods=['GET'])
def get_replicas():
    return jsonify({
        "N": len(servers),
        "replicas": servers
    })


@app.route('/add', methods=['POST'])
def add_servers():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        return jsonify({"error": "Number of hostnames exceeds the number of instances to add"}), 400

    new_servers = []
    for i in range(n):
        hostname = hostnames[i] if i < len(
            hostnames) else f"server-{random.randint(1000, 9999)}"
        new_servers.append(hostname)
        container = client.containers.run(
            "my_web_server_image",
            name=hostname,
            detach=True,
            environment={"SERVER_ID": hostname.split('-')[-1]}
        )
        servers.append(hostname)
        ch.add_server(hostname)

    return jsonify({
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    })


@app.route('/rm', methods=['DELETE'])
def remove_servers():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
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
        to_remove = random.sample(servers, n)

    for hostname in to_remove:
        container = client.containers.get(hostname)
        container.stop()
        container.remove()
        servers.remove(hostname)
        ch.remove_server(hostname)

    return jsonify({
        "message": {
            "N": len(servers),
            "replicas": servers
        },
        "status": "successful"
    })


@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    server = ch.get_server(path)
    if server:
        container = client.containers.get(server)
        response = container.exec_run(f"curl -s http://localhost:5000/{path}")
        return response.output.decode('utf-8')
    else:
        return "No servers available", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

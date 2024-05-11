#import necessary libraries
from flask import Flask,jsonify
import os

#create a flask application instance
app= Flask(__name__)

#define a route for the index page
@app.route('/')
def index():
#define html content for the index page
    html_content="""<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Click the link below to go to the home page:</p>
    <a href="home">Go to Home</a>
    <a href="heartbeat">Go to Heartbeat</a>
</body>
</html>
"""
      
    #return the html content as a reponse with status code 200
    return html_content,200


#define a route for home endpount with GET method
@app.route('/home',methods=['GET'])
def home():

    #get server ID from environment variable 'SERVER ID' and default to 0 if not sent
    server_id =os.getenv('SERVER_ID','0')
   #return a json message with server id, status successful and 200 status code
    return jsonify(message=f'Hello from Server:{server_id}',status='successful'),200

#define route for heartbeat endpoint
@app.route('/heartbeat',methods=['GET'])
def heartbeat():
   #return an empty reponse with status code 200
     return'',200
    

#start the Flask server listening on all network interfaces
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)


#import necessary libraries
from flask import Flask,jsonify
import os

server= Flask(__name__)


@server.route('/')
def index():

    html_content="""" <!DOCTYPE html>
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
      
    return html_content,200

@server.route('/home',methods=['GET'])
def home():

    server_id =os.getenv('SERVER_ID','0')
    return jsonify(message=f'Hello from Server:{server_id}',status='successful'),200

@server.route('/heartbeat',methods=['GET'])
def heartbeat():
    return'',200
    

if __name__=='__main__':
    server.run(host='0.0.0.0',port=5000)


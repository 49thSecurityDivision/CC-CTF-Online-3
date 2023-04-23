#!/usr/bin/python3
from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

creds = {
    "x-api-key" : "not_the_api_key",
}

data = {
    "flag": "flag{the_end_but_not_over}"
}

authed = "welcome_home_roscoe_jenkins"

@app.route('/token', methods=['POST'])
def get_token():
    auth_header = request.headers.get('Authorization')
    client_id, client_secret = base64.b64decode(auth_header.split(' ')[1]).decode().split(':')

    if creds["x-api-key"] == client_secret:
        return jsonify({'secret': authed })
    else:
        return jsonify({'error': 'invalid_client'}), 401

@app.route('/data', methods=['GET'])
def get_privileged_data():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(' ')[1]
        if token == authed:
            return jsonify(data)
    return jsonify({'error': 'invalid_token'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

#!/usr/bin/python3
from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

creds = {
    "client_id" : "not_admin",
    "client_secret" : "access"
}

data = {
    "flag": "flag{silly_haxor_admin}"
}

bearer = "secret_admin_key123"

@app.route('/token', methods=['POST'])
def get_token():
    auth_header = request.headers.get('Authorization')
    client_id, client_secret = base64.b64decode(auth_header.split(' ')[1]).decode().split(':')

    if creds["client_id"] == client_id:
        return jsonify({'bearer': bearer})
    else:
        return jsonify({'error': 'invalid_client'}), 401

@app.route('/data', methods=['GET'])
def get_privileged_data():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        access_token = auth_header.split(' ')[1]
        client_id = access_token[::-1]
        if client_id in creds and creds[client_id] == access_token:
            return jsonify(data)
    return jsonify({'error': 'invalid_token'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

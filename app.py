from flask import Flask, request, jsonify
import requests as r
import socket


hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

app = Flask(__name__)

'''
ping sends {'msg': 'something'}
pong returns {'msg': 'replying something from {ip}'}
'''
@app.route('/ping', methods=['POST'])
def ping():
    payload = request.json
    with r.Session() as conn:
        resp = conn.post(
            payload['url'],
            json=payload['payload']
        )
    return jsonify(resp)

@app.route('/pong', methods=['POST'])
def ping():
    payload = request.json
    return jsonify(
        {'msg': f'replying {hostname}@{IPAddr} with {payload["msg"]}'}
    )

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)
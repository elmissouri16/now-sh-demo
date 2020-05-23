from flask import Flask, jsonify, Response
import requests
app = Flask(__name__)
@app.route('/', methods=['GET'])
def getme():
    rsp = requests.get('https://api.kanye.rest/?format=json')
    return jsonify(rsp.content)
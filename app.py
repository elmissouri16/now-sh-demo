from flask import Flask, jsonify, Response, request
app = Flask(__name__)
@app.route('/', methods=['GET'])
def getme():
   
    return str('working')
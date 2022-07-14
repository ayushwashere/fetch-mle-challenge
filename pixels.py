from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/")
def intro():
    res = {
        "author": "Ayush Kumar",
        "usage": ""
    }
    return jsonify(res)



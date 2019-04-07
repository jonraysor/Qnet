from flask import Flask,jsonify
import pandas

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hi2'


@app.route('/ ')
def getAllSchools():
    return jsonify([])

app.run()

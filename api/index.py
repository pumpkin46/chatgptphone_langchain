import os
from flask import Flask, request, jsonify
from flask import Flask
from langchain.llms import OpenAI

app = Flask(__name__)

@app.route('/getAnswer')
def getAnswer():
    try:
        llm = OpenAI(temperature=0.9)
        result = llm(request.form["question"])
        return jsonify({'message': result}), 200
    except Exception as err:
        return jsonify({'message': 'Langchain Error'}), 401


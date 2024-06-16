#! C:\RENDY\Coding\EPosyandu\model\myenv\Scripts\python.exe

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pickle
import sklearn
import sklearn.metrics
import os

app = Flask(__name__)
CORS(app)

# Load model
file_path = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
# file_path = 'C:/RENDY/Coding/EPosyandu/model/model.pkl'
with open(file_path , 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return "Flask Server - Posyandu Line"

# Endpoint untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    umur = int(data['umur'])
    jenis_kelamin = int(data['jenis_kelamin'])
    tinggi_badan = float(data['tinggi_badan'])
    input_features = [umur, jenis_kelamin, tinggi_badan]
    prediction = model.predict([input_features])[0]
    prediction = int(prediction)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

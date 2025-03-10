import pickle
from flask import Flask, request, jsonify, render_template, url_for
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and the scaler
model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For rendering results on HTML GUI
    '''
    data = request.json['data']
    new_data = np.array(list(data.values())).reshape(1, -1)
    new_data = scaler.transform(new_data)
    prediction = model.predict(new_data)
    output = round(prediction[0], 2)
    return jsonify(output)

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1, -1))
    prediction = model.predict(final_input)
    output = round(prediction[0], 2)
    return render_template('home.html', prediction_text='The Predicted House Price: {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)

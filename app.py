# app.py

from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model
with open('iris_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Convert data into numpy array
    input_features = np.array([data['features']])

    # Make prediction
    prediction = model.predict(input_features)

    # Create a response object
    output = {'prediction': int(prediction[0])}
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)

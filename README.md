# Iris Flower Classification API

This project demonstrates how to train a machine learning model using the Iris dataset and deploy it using Flask as a web API.

## Project Structure

- `Iris_Classification_model.ipynb`: Jupyter notebook to train the RandomForest model.
- `app.py`: Flask application to serve the model as an API.
- `iris_model.pkl`: Serialized model saved using pickle.
- `requirements.txt`: List of dependencies to run the project.
- `README.md`: Project overview and instructions.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/iris-flower-classification-api.git
    cd iris-flower-classification-api
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Train the model**:
    - Open `model_training.ipynb` in a Jupyter notebook and run the cells to train the model.
    - This will save the model as `iris_model.pkl`.

4. **Run the Flask application**:
    ```bash
    python app.py
    ```

5. **Test the API**:
    - You can use `curl` or Postman to send a POST request to the `/predict` endpoint.
    - Example request:
      ```bash
      curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
      ```
    - Expected response:
      ```json
      {"prediction": 0}
      ```

## Project Explanation

The project trains a simple RandomForest model on the Iris dataset to classify flowers into three species. The trained model is then exposed through a Flask API that accepts POST requests with input features and returns the predicted class.

The API is a basic example of how machine learning models can be deployed in production and accessed via HTTP requests.

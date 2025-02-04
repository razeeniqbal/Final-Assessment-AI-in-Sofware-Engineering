from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = model.predict(np.array([data["features"]]))
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

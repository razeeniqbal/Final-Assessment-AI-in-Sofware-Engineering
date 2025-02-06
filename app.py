from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        data = request.json
        df = pd.DataFrame(data)
        
        # Make predictions
        prediction = model.predict(df)
        
        # Return the prediction as JSON
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

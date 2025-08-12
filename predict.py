# Load the packages
import pickle
from flask import Flask, request, jsonify
import pandas as pd

# Load the model (saved earlier from MLflow version 3)
with open('lr_model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

# Feature preparation function
def prepare_features(car):
    return pd.DataFrame([{
        'cylinders': car['cylinders'],
        'displacement': car['displacement'],
        'horsepower': car['horsepower'],
        'weight': car['weight'],
        'acceleration': car['acceleration'],
        'model_year': car['model_year'],
        'origin': car['origin']
    }])

# Prediction function
def predict(features_df):
    preds = model.predict(features_df)
    return float(preds[0])

# Create Flask app
app = Flask('mpg-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    car = request.get_json()
    features_df = prepare_features(car)
    pred = predict(features_df)
    result = {
        'predicted_mpg': pred
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)



 
 
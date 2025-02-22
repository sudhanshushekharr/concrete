
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('concrete_strength_model.pkl')
scaler = joblib.load('concrete_strength_scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from JSON request
        data = request.json
        
        # Convert input to numpy array
        input_features = np.array([
            data['Cement'], data['Blast_furn_slag'], data['Fly_Ash'], 
            data['Water'], data['Superplasticizer'], data['Coarse_Agg'], 
            data['fine_Agg'], data['Age']
        ]).reshape(1, -1)
        
        # Scale the input
        scaled_features = scaler.transform(input_features)
        
        # Predict
        prediction = model.predict(scaled_features)[0]
        
        return jsonify({'predicted_strength': float(prediction)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
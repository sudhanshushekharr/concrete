import streamlit as st
import requests
import json

def predict_concrete_strength(cement, blast_slag, fly_ash, water, 
                               superplasticizer, coarse_agg, fine_agg, age):
    # Prepare data for API call
    data = {
        'Cement': cement,
        'Blast_furn_slag': blast_slag,
        'Fly_Ash': fly_ash,
        'Water': water,
        'Superplasticizer': superplasticizer,
        'Coarse_Agg': coarse_agg,
        'fine_Agg': fine_agg,
        'Age': age
    }
    
    # Make API call
    try:
        response = requests.post('http://localhost:5000/predict', 
                                 json=data, 
                                 headers={'Content-Type': 'application/json'})
        result = response.json()
        return result['predicted_strength']
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

def main():
    # Set page title and icon
    st.set_page_config(page_title="Concrete Strength Predictor", page_icon="🏗️")
    st.title('Concrete Strength Predictor')
    
    # Input fields
    cement = st.number_input('Cement (kg/m³)', min_value=0.0, step=0.1)
    blast_slag = st.number_input('Blast Furnace Slag (kg/m³)', min_value=0.0, step=0.1)
    fly_ash = st.number_input('Fly Ash (kg/m³)', min_value=0.0, step=0.1)
    water = st.number_input('Water (kg/m³)', min_value=0.0, step=0.1)
    superplasticizer = st.number_input('Superplasticizer (kg/m³)', min_value=0.0, step=0.1)
    coarse_agg = st.number_input('Coarse Aggregate (kg/m³)', min_value=0.0, step=0.1)
    fine_agg = st.number_input('Fine Aggregate (kg/m³)', min_value=0.0, step=0.1)
    age = st.number_input('Age (days)', min_value=1, step=1)
    
    if st.button('Predict Concrete Strength'):
        prediction = predict_concrete_strength(
            cement, blast_slag, fly_ash, water, 
            superplasticizer, coarse_agg, fine_agg, age
        )
        
        if prediction is not None:
            st.success(f'Predicted Concrete Strength: {prediction:.2f} MPa')

if __name__ == '__main__':
    main()
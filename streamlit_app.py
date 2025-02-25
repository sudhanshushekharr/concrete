import streamlit as st
import requests
import json
import qrcode
from io import BytesIO
import base64
from datetime import datetime

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

        
        # Replace 'your_server_ip_or_domain' with the actual IP address or domain name
        response = requests.post('https://concretestrentgh.streamlit.app/predict',
                                 json=data,
                                 headers={'Content-Type': 'application/json'})
        result = response.json()
        return result['predicted_strength']
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None



def generate_html_content(mix_data):
    """Generate HTML content for displaying mix data"""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Concrete Mix Details</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        .header {{
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
        }}
        .content {{
            border: 1px solid #ddd;
            border-top: none;
            padding: 20px;
            border-radius: 0 0 5px 5px;
            background-color: #f9f9f9;
        }}
        .mix-info {{
            margin-bottom: 20px;
        }}
        .mix-details {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }}
        .mix-column {{
            flex: 1;
            min-width: 250px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        .strength-value {{
            font-size: 24px;
            font-weight: bold;
            color: #2980b9;
        }}
        .timestamp {{
            font-size: 12px;
            color: #7f8c8d;
            text-align: right;
            margin-top: 20px;
        }}
        .notes {{
            background-color: #fcf8e3;
            padding: 10px;
            border-left: 5px solid #faebcc;
            margin-top: 20px;
        }}
        @media print {{
            body {{
                font-size: 12px;
            }}
            .header {{
                background-color: #eee !important;
                color: black !important;
            }}
            .no-print {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h2>Concrete Mix Details</h2>
        <p>{mix_data.get('Mix_Name', 'Unnamed Mix')}</p>
    </div>
    
    <div class="content">
        <div class="mix-info">
            <h3>Project Information</h3>
            <table>
                <tr>
                    <th>Project</th>
                    <td>{mix_data.get('Project', 'N/A')}</td>
                </tr>
                <tr>
                    <th>Location</th>
                    <td>{mix_data.get('Location', 'N/A')}</td>
                </tr>
                <tr>
                    <th>Mix ID</th>
                    <td>{mix_data.get('Mix_Name', 'N/A')}</td>
                </tr>
                <tr>
                    <th>Generated On</th>
                    <td>{mix_data.get('generated_on', 'N/A')}</td>
                </tr>
            </table>
        </div>
        
        <div class="mix-details">
            <div class="mix-column">
                <h3>Mix Composition</h3>
                <table>
                    <tr><th>Material</th><th>Amount (kg/m³)</th></tr>
                    <tr><td>Cement</td><td>{mix_data.get('Cement', 0)}</td></tr>
                    <tr><td>Blast Furnace Slag</td><td>{mix_data.get('Blast_Furnace_Slag', 0)}</td></tr>
                    <tr><td>Fly Ash</td><td>{mix_data.get('Fly_Ash', 0)}</td></tr>
                    <tr><td>Water</td><td>{mix_data.get('Water', 0)}</td></tr>
                    <tr><td>Superplasticizer</td><td>{mix_data.get('Superplasticizer', 0)}</td></tr>
                    <tr><td>Coarse Aggregate</td><td>{mix_data.get('Coarse_Aggregate', 0)}</td></tr>
                    <tr><td>Fine Aggregate</td><td>{mix_data.get('Fine_Aggregate', 0)}</td></tr>
                </table>
            </div>
            
            <div class="mix-column">
                <h3>Strength Properties</h3>
                <table>
                    <tr>
                        <th>Predicted Strength (MPa)</th>
                    </tr>
                    <tr>
                        <td class="strength-value">{mix_data.get('Predicted_Strength', 'N/A')}</td>
                    </tr>
                </table>
                
                <h4>Curing Age</h4>
                <table>
                    <tr><th>Age (days)</th><td>{mix_data.get('Age', 'N/A')}</td></tr>
                </table>
            </div>
        </div>
        
        {f'<div class="notes"><h3>Notes</h3><p>{mix_data.get("Notes")}</p></div>' if mix_data.get('Notes') else ''}
        
        <div class="timestamp">Generated with Concrete Strength Predictor</div>
        
        <button class="no-print" onclick="window.print()">Print this page</button>
    </div>
</body>
</html>'''
    return html

def generate_qr_code(url_or_data):
    """Generate a QR code containing a URL or minimal data"""
    # Create QR code
    qr = qrcode.QRCode(
        version=None,  # Will auto-determine
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
        box_size=10,
        border=4,
    )
    qr.add_data(url_or_data)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to bytes
    buffered = BytesIO()
    img.save(buffered)
    return base64.b64encode(buffered.getvalue()).decode()

def main():
    # Set page title and icon
    st.set_page_config(page_title="Concrete Strength Predictor", page_icon="🏗️")
    st.title('Concrete Strength Predictor')
    
    # Create tabs for different sections
    tab1, tab2 = st.tabs(["Prediction", "Documentation"])
    
    with tab1:
        # Input fields
        col1, col2 = st.columns(2)
        
        with col1:
            cement = st.number_input('Cement (kg/m³)', min_value=0.0, step=0.1)
            blast_slag = st.number_input('Blast Furnace Slag (kg/m³)', min_value=0.0, step=0.1)
            fly_ash = st.number_input('Fly Ash (kg/m³)', min_value=0.0, step=0.1)
            water = st.number_input('Water (kg/m³)', min_value=0.0, step=0.1)
        
        with col2:
            superplasticizer = st.number_input('Superplasticizer (kg/m³)', min_value=0.0, step=0.1)
            coarse_agg = st.number_input('Coarse Aggregate (kg/m³)', min_value=0.0, step=0.1)
            fine_agg = st.number_input('Fine Aggregate (kg/m³)', min_value=0.0, step=0.1)
            age = st.number_input('Age (days)', min_value=1, step=1)
        
        # Mix name and project details
        mix_name = st.text_input("Mix Name/ID", "Mix-1")
        project_name = st.text_input("Project Name", "")
        location = st.text_input("Location", "")
        
        # Store the current mix in session state
        if 'current_mix' not in st.session_state:
            st.session_state.current_mix = {}
            st.session_state.predicted_strength = None
        
        if st.button('Predict Concrete Strength'):
            prediction = predict_concrete_strength(
                cement, blast_slag, fly_ash, water, 
                superplasticizer, coarse_agg, fine_agg, age
            )
            
            if prediction is not None:
                st.session_state.predicted_strength = prediction
                st.success(f'Predicted Concrete Strength: {prediction:.2f} MPa')
                
                # Store the current mix
                st.session_state.current_mix = {
                    'Mix_Name': mix_name,
                    'Project': project_name,
                    'Location': location,
                    'Cement': cement,
                    'Blast_Furnace_Slag': blast_slag,
                    'Fly_Ash': fly_ash,
                    'Water': water,
                    'Superplasticizer': superplasticizer,
                    'Coarse_Aggregate': coarse_agg,
                    'Fine_Aggregate': fine_agg,
                    'Age': age,
                    'Predicted_Strength': f"{prediction:.2f} MPa"
                }
    
    with tab2:
        st.header("Mix Documentation")
        
        if st.session_state.current_mix and st.session_state.predicted_strength is not None:
            # Display mix information
            st.subheader("Current Mix Details")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Mix Name:** {st.session_state.current_mix['Mix_Name']}")
                st.write(f"**Project:** {st.session_state.current_mix['Project']}")
                st.write(f"**Location:** {st.session_state.current_mix['Location']}")
                st.write(f"**Predicted Strength:** {st.session_state.current_mix['Predicted_Strength']}")
            
            with col2:
                st.write("**Mix Composition:**")
                st.write(f"- Cement: {st.session_state.current_mix['Cement']} kg/m³")
                st.write(f"- Blast Furnace Slag: {st.session_state.current_mix['Blast_Furnace_Slag']} kg/m³")
                st.write(f"- Fly Ash: {st.session_state.current_mix['Fly_Ash']} kg/m³")
                st.write(f"- Water: {st.session_state.current_mix['Water']} kg/m³")
                st.write(f"- Superplasticizer: {st.session_state.current_mix['Superplasticizer']} kg/m³")
                st.write(f"- Coarse Aggregate: {st.session_state.current_mix['Coarse_Aggregate']} kg/m³")
                st.write(f"- Fine Aggregate: {st.session_state.current_mix['Fine_Aggregate']} kg/m³")
                st.write(f"- Age: {st.session_state.current_mix['Age']} days")
            
            # Add notes field
            notes = st.text_area("Additional Notes", "", help="Add any special instructions or observations")
            
            # Create documentation
            if st.button("Generate Documentation"):
                # Add notes and timestamp to the mix data
                mix_data = st.session_state.current_mix.copy()
                mix_data['Notes'] = notes
                mix_data['generated_on'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Generate HTML content
                html_content = generate_html_content(mix_data)
                
                # Download HTML button
                st.download_button(
                    label="Download Mix Details (HTML)",
                    data=html_content,
                    file_name=f"concrete_mix_{mix_data['Mix_Name'].replace(' ', '_')}.html",
                    mime="text/html"
                )
                
                # Generate compact QR code with just essential info
                compact_data = {
                    'id': mix_data['Mix_Name'],
                    'strength': mix_data['Predicted_Strength'],
                    'age': mix_data['Age'],
                    'date': mix_data['generated_on']
                }
                qr_data = json.dumps(compact_data)
                qr_code = generate_qr_code(qr_data)
                
                # Display QR code
                st.image(f"data:image/png;base64,{qr_code}", caption="Scan this QR code for mix ID")
                
                # Add download button for QR code
                st.download_button(
                    label="Download QR Code",
                    data=base64.b64decode(qr_code),
                    file_name=f"concrete_mix_{mix_data['Mix_Name'].replace(' ', '_')}_qr.png",
                    mime="image/png"
                )
                
                # Text explanation
                st.info("The HTML file contains all mix details in a mobile-friendly format. You can download and share it via email or cloud storage. The QR code contains basic mix identification information.")
                
                # Preview section
                with st.expander("Preview How the HTML Will Look"):
                    st.components.v1.html(html_content, height=600)
        else:
            st.warning("Please predict a mix first in the 'Prediction' tab before generating documentation.")

if __name__ == '__main__':
    main()
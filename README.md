# Concrete Strength Predictor 🏗️

A comprehensive machine learning application that predicts concrete compressive strength based on mix composition parameters. This project combines a Flask API backend with a Streamlit frontend to provide an intuitive interface for civil engineers and construction professionals.

## 🚀 Features

### Core Functionality
- **Concrete Strength Prediction**: Predict compressive strength (MPa) based on 8 key mix parameters
- **Real-time API**: RESTful API endpoint for programmatic access
- **Interactive Web Interface**: User-friendly Streamlit dashboard
- **Mix Documentation**: Generate detailed HTML reports with mix specifications
- **QR Code Generation**: Create QR codes for easy mix identification and tracking

### Input Parameters
- **Cement** (kg/m³)
- **Blast Furnace Slag** (kg/m³)
- **Fly Ash** (kg/m³)
- **Water** (kg/m³)
- **Superplasticizer** (kg/m³)
- **Coarse Aggregate** (kg/m³)
- **Fine Aggregate** (kg/m³)
- **Age** (days)

### Output Features
- **Predicted Strength**: Compressive strength in MPa
- **Mix Documentation**: Professional HTML reports
- **QR Codes**: Compact identification codes
- **Project Tracking**: Mix naming and project organization

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: Streamlit (Python web app framework)
- **Machine Learning**: Scikit-learn, XGBoost
- **Data Processing**: NumPy, Pandas
- **QR Code Generation**: qrcode library
- **API Communication**: Requests library
- **CORS Support**: Flask-CORS

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd concrete
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify model files**
   Ensure the following files are present in the project directory:
   - `concrete_strength_model.pkl` (trained ML model)
   - `concrete_strength_scaler.pkl` (feature scaler)

## 🚀 Usage

### Option 1: Web Application (Recommended)

1. **Start the Flask API server**
   ```bash
   python flask_app.py
   ```
   The API will be available at `http://localhost:5002`

2. **Start the Streamlit application**
   ```bash
   streamlit run streamlit_app.py
   ```
   The web interface will open at `http://localhost:8501`

3. **Use the application**
   - Navigate to the "Prediction" tab
   - Enter mix composition parameters
   - Click "Predict Concrete Strength"
   - View results and generate documentation

### Option 2: API Only

If you only need the prediction API:

```bash
python flask_app.py
```

Then make POST requests to `http://localhost:5002/predict` with JSON data:

```json
{
    "Cement": 350.0,
    "Blast_furn_slag": 0.0,
    "Fly_Ash": 0.0,
    "Water": 180.0,
    "Superplasticizer": 0.0,
    "Coarse_Agg": 1000.0,
    "fine_Agg": 800.0,
    "Age": 28
}
```

## 📊 Application Structure

### Flask API (`flask_app.py`)
- **Port**: 5002
- **Endpoint**: `/predict` (POST)
- **Functionality**: Loads trained model and scaler, processes input data, returns predictions
- **CORS**: Enabled for cross-origin requests

### Streamlit App (`streamlit_app.py`)
- **Port**: 8501 (default)
- **Tabs**: 
  - **Prediction**: Input form and strength prediction
  - **Documentation**: Mix details and report generation

### Key Functions
- `predict_concrete_strength()`: Makes API calls to Flask backend
- `generate_html_content()`: Creates professional HTML reports
- `generate_qr_code()`: Generates QR codes for mix identification

## 📁 Project Structure

```
concrete/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── flask_app.py                # Flask API server
├── streamlit_app.py            # Streamlit web interface
├── concrete_strength_model.pkl  # Trained ML model
├── concrete_strength_scaler.pkl # Feature scaler
└── .git/                       # Git repository
```

## 🔍 Model Information

- **Algorithm**: XGBoost (based on dependencies)
- **Input Features**: 8 numerical parameters
- **Output**: Compressive strength in MPa
- **Preprocessing**: Feature scaling applied
- **Model Files**: 
  - `concrete_strength_model.pkl`: Trained model
  - `concrete_strength_scaler.pkl`: StandardScaler for feature normalization

## 📈 Usage Examples

### Typical Mix Parameters
```python
# Standard concrete mix
cement = 350.0          # kg/m³
blast_slag = 0.0        # kg/m³
fly_ash = 0.0           # kg/m³
water = 180.0           # kg/m³
superplasticizer = 0.0  # kg/m³
coarse_agg = 1000.0     # kg/m³
fine_agg = 800.0        # kg/m³
age = 28                # days
```

### Expected Output
- **Predicted Strength**: ~30-50 MPa (typical range)
- **HTML Report**: Professional documentation with mix details
- **QR Code**: Compact identification for field use

## 🎯 Use Cases

- **Civil Engineering**: Quick strength estimation during design phase
- **Construction**: On-site mix validation and quality control
- **Research**: Academic studies on concrete mix optimization
- **Quality Assurance**: Documentation and tracking of mix designs

## 🔧 Customization

### Adding New Features
1. **Model Retraining**: Replace `concrete_strength_model.pkl` with updated model
2. **UI Modifications**: Edit `streamlit_app.py` for interface changes
3. **API Extensions**: Add new endpoints in `flask_app.py`

### Configuration
- **API Port**: Modify port in `flask_app.py` (default: 5002)
- **Streamlit Port**: Use `streamlit run --server.port <port>` for custom port
- **Model Path**: Update model loading paths if files are moved

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Kill process using port 5002
   lsof -ti:5002 | xargs kill -9
   ```

2. **Model Files Missing**
   - Ensure `concrete_strength_model.pkl` and `concrete_strength_scaler.pkl` are in the project directory

3. **Dependencies Issues**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

4. **CORS Errors**
   - Verify Flask-CORS is installed and enabled in `flask_app.py`

### Debug Mode
- Flask API runs in debug mode by default
- Check console output for detailed error messages
- Streamlit provides real-time error feedback

## 📝 License

This project is open source. Please check the repository for specific licensing information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Open an issue in the repository

---

**Built with ❤️ for the construction industry** 
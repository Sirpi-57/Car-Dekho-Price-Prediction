import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

# Load scaler and XGBoost model from pickle files
with open('scaler1.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('xgb_model1.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

# Initialize session state to manage pages
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Function to show the prediction page
def show_prediction_page():
    st.title('Used Car Price Prediction and Selection:')

    # Input fields (your existing code)
    insurance_validity_map = {'Comprehensive': 3, 'Third Party': 2, 'Zero Dep': 1, 'Not Available': 0}
    insurance_validity = st.selectbox("Insurance Validity", options=list(insurance_validity_map.keys()))
    insurance_encoded = insurance_validity_map[insurance_validity]

    fuel_type_map = {'Diesel': 5, 'Petrol': 4, 'CNG': 3, 'Electric': 2, 'LPG': 1}
    fuel_type = st.selectbox("Fuel Type", options=list(fuel_type_map.keys()))
    fuel_encoded = fuel_type_map[fuel_type]

    owner_no_map = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
    owner_no = st.selectbox("Owner Number", options=list(owner_no_map.keys()))
    owner_encoded = owner_no_map[owner_no]

    displacement = st.slider("Displacement (cc)", min_value=750, max_value=2000, step=1)
    mileage = st.slider("Mileage (kmpl)", min_value=10.0, max_value=30.0, step=0.01)
    torque = st.slider("Torque (Nm)", min_value=5.0, max_value=350.0, step=0.1)
    vehicle_age = st.number_input("Vehicle Age (years)", min_value=0)
    reg_age = st.number_input("Registered Age (years)", min_value=0)

    km = st.slider("Kilometers Driven", min_value=600, max_value=150000, step=100)
    km_sqrt = np.sqrt(km)

    max_power = st.slider("Max Power (bhp)", min_value=30.0, max_value=180.0, step=0.1)
    max_power_sqrt = np.sqrt(max_power)

    seats_options = [7, 5, 6, 4, 8, 10]
    seats_1 = st.selectbox("Number of Seats", options=seats_options)

    bt_options = ['Convertibles', 'Coupe', 'Hatchback', 'Hybrids', 'MUV', 'Minivans', 'Pickup Trucks', 'SUV', 'Sedan', 'Wagon']
    bt = st.selectbox("Body Type", options=bt_options)
    bt_encoded = {f'bt_{option}': 0 for option in bt_options[1:]}  
    if bt != bt_options[0]:  
        bt_encoded[f'bt_{bt}'] = 1

    transmission_options = ['Automatic', 'Manual']
    transmission = st.selectbox("Transmission", options=transmission_options)
    transmission_encoded = {f'transmission_{option}': 0 for option in transmission_options[1:]}  
    if transmission != transmission_options[0]:  
        transmission_encoded[f'transmission_{transmission}'] = 1

    state_options = ['Andhra Pradesh', 'Chandigarh', 'Delhi', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                     'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Odisha',
                     'Pondicherry', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh',
                     'Uttarakhand', 'West Bengal']
    state = st.selectbox("State", options=state_options)
    state_encoded = {f'state_{option}': 0 for option in state_options[1:]}  
    if state != state_options[0]:  
        state_encoded[f'state_{state}'] = 1

    # Combine all inputs into a DataFrame
    input_data = {
        'Insurance Validity': [insurance_encoded],
        'Fuel Type': [fuel_encoded],
        'ownerNo': [owner_encoded],
        'Displacement': [displacement],
        'Mileage': [mileage],
        'Torque': [torque],
        'Seats_1': [seats_1],
        'vehicle_age': [vehicle_age],
        'reg_age': [reg_age],
        'km_sqrt': [km_sqrt],
        'Max Power_sqrt': [max_power_sqrt]
    }

    # Convert dictionary to DataFrame
    df = pd.DataFrame(input_data)

    # Concatenate manually created one-hot encoded columns
    bt_df = pd.DataFrame(bt_encoded, index=[0])
    transmission_df = pd.DataFrame(transmission_encoded, index=[0])
    state_df = pd.DataFrame(state_encoded, index=[0])

    df = pd.concat([df, bt_df, transmission_df, state_df], axis=1)

    # Scale the input DataFrame
    scaled_input_df = scaler.transform(df)

    # Predict using the XGBoost model
    predicted_price_xgb_scaled = xgb_model.predict(scaled_input_df)

    # Display the predicted price
    st.markdown(f"<h2 style='text-align: center;'>Predicted Price: ₹{predicted_price_xgb_scaled[0]:,.2f}</h2>", unsafe_allow_html=True)

# Function to show the welcome page
def show_welcome_page():
    st.title("Welcome to Car Dekho Price Prediction!")
    st.image("welcome_page_image.jpg") 
    if st.button("Let's Go"):
        st.session_state.page = 'prediction'

# Streamlit app configuration
icon = "page_icon.png"
st.set_page_config(page_title="CarDekho Price Prediction", page_icon=icon)

# Initializing session state
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Welcome To Used Car Price Prediction App!</h1>
            <h3>"IT ALL STARTS WITH A DREAM"</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Center the button using Streamlit
    col1, col2, col3 = st.columns([10, 12, 4])
    with col2:
        if st.button("Let's Go"):
            st.session_state.page = 'prediction'

    # Center an image below the button
    col1, col2, col3 = st.columns([0.5, 2000, 0.5])  
    with col2:
        st.image("pre-owned-banner.jpg")
else:
    show_prediction_page()
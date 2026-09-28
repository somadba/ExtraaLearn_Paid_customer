
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("extraalearn_edtech_model_v1_0.joblib")

model = load_model()

# Streamlit UI for Price Prediction
st.title("ExtraaLearn EdTech Paid Customer App")
st.write("This tool predicts converting to a paid customer based on the customer details.")

st.subheader("Enter the customer details:")

# Collect user input
age = st.number_input("Age", min_value=1, max_value=100, value=30)
current_occupation = st.selectbox("Current Occupation", ["Student", "Professional", "Unemployed"])
first_interaction = st.selectbox("Social media first_interaction", ["Website", "Mobile App", "Email"])
profile_completed = st.selectbox("Profile Completed", ["High", "Medium","Low"])
website_visits = st.number_input("Number of Website Visits", min_value=0, step=1, value=0)
time_spent_on_website = st.number_input("Time Spent on Website", min_value=0, step=1, value=0)
page_views_per_visit = st.number_input("Page Views per Visit", min_value=0, step=1, value=0)
last_activity = st.selectbox("Last Activity", ["Email", "Mobile App", "Website"])
print_media_type1 = st.selectbox("Print Media Type 1", ["Yes", "No"])
print_media_type2 = st.selectbox("Print Media Type 2", ["Yes", "No"])
digital_media = st.selectbox("Digital Media", ["Yes", "No"])
educational_channels = st.selectbox("Educational Channels", ["Yes", "No"])
referral = st.selectbox("Referral", ["Yes", "No"])


# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    'age': age,
    'current_occupation': current_occupation,
    'first_interaction': first_interaction,
    'profile_completed': profile_completed,
    'website_visits': website_visits,
    'time_spent_on_website': time_spent_on_website,
    'page_views_per_visit': page_views_per_visit,
    'last_activity': last_activity,
    'print_media_type1': print_media_type1,
    'print_media_type2': print_media_type2,
    'digital_media': digital_media,
    'educational_channels': educational_channels,
    'referral': referral
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Converted to Paid  ${(prediction)[0]:.2f}.")

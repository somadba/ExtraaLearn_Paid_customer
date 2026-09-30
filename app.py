
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
website_visits = st.number_input("Number of Website Visits", min_value=0, step=1, value=0)
time_spent_on_website = st.number_input("Time Spent on Website", min_value=0, step=1, value=0)
page_views_per_visit = st.number_input("Page Views per Visit", min_value=0, step=1, value=0)
current_occupation_Student=st.selectbox("Current Occupation - A Student?", ["true", "false"])
current_occupation_Unemployed=st.selectbox("Current Occupation - Unemployed?", ["true", "false"])
first_interaction_Website=st.selectbox("first_interaction - Website?", ["true", "false"])
profile_completed_Low=st.selectbox("Profile Completed - Low?", ["true", "false"])
profile_completed_Medium=st.selectbox("Profile Completed - Medium?", ["true", "false"])
last_activity_Phone_Activity=st.selectbox("last_activity - Phone Activity?", ["true", "false"])
last_activity_Website_Activity=st.selectbox("last_activity - Website Activity?", ["true", "false"])
print_media_type1_Yes=st.selectbox("print_media_type1 - Yes?", ["true", "false"])
print_media_type2_Yes=st.selectbox("print_media_type2 - Yes?", ["true", "false"])
digital_media_Yes=st.selectbox("digital_media - Yes?", ["true", "false"])
educational_channels_Yes=st.selectbox("educational_channels - Yes?", ["true", "false"])
referral_Yes=st.selectbox("referral - Yes?", ["true", "false"])


# Convert user input into a DataFrame
input_data = pd.DataFrame([{
'age': age,
'website_visits': website_visits,
'time_spent_on_website': time_spent_on_website,
'page_views_per_visit': page_views_per_visit,
'current_occupation_Student': current_occupation_Student,
'current_occupation_Unemployed': current_occupation_Unemployed,
'first_interaction_Website': first_interaction_Website,
'profile_completed_Low': profile_completed_Low,
'profile_completed_Medium': profile_completed_Medium,
'last_activity_Phone_Activity': last_activity_Phone_Activity ,
'last_activity_Website_Activity': last_activity_Website_Activity,
'print_media_type1_Yes': print_media_type1_Yes,
'print_media_type2_Yes': print_media_type2_Yes,
'digital_media_Yes': digital_media_Yes,
'educational_channels_Yes': educational_channels_Yes,
'referral_Yes': referral_Yes
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Converted to Paid  ${(prediction)[0]:.2f}.")

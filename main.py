import streamlit as st
import pandas as pandas
from joblib import load
model = load("my_telco_trained_model.joblib")
st.title("Telecom Customer Churn Prediction App")
st.header("Enter Customer Information")

tenure = st.number_input("Tenure in months", min_value = 0, max_value=100, value=1)
internet_service = st.selectbox("Internet Service", ("DSL", "Fiber_Optic", "No"))
contract = st.selectbox("Contract", ("Month", "year1", "year2"))
monthly_charges = st.number_input("Monthly Charges", min_value = 0, max_value=500, value=1)
total_charges = st.number_input("Total Charges", min_value = 0, max_value=10000, value=1)

if internet_service == "DSL":
    internet_service_arr = [1, 0, 0]
elif internet_service == "Fiber_Optic":
    internet_service_arr = [0, 1, 0]
else:
    internet_service_arr = [0, 0, 1]


if contract == "Month":
    contract_arr = [1, 0, 0]
elif contract == "year1":
    contract_arr = [0, 1, 0]
else:
    contract_arr = [0, 0, 1]

input_arr = []
input_arr.append(tenure)
input_arr.append(monthly_charges)
input_arr.append(total_charges)
input_arr += internet_service_arr
input_arr += contract_arr

print(input_arr)

prediction = model.predict([input_arr])

print(prediction[0])

st.header("Prediction Result")
if prediction[0] == 0:
    st.success("This customer is likely to stay")
else:
    st.success("This customer is going to leave")










import streamlit as st
from datetime import datetime, timedelta

st.title("Advanced State Management")

# Store widget value in session state
st.subheader("Store widget value in session state")

st.slider(label="Slifer",min_value=0,max_value=10,value=5,key="slider")
slider = st.session_state["slider"]
st.write(slider)

st.date_input(label="StartDate",key="minDate")
minDate =st.session_state["minDate"]
st.write(minDate)

# Initialize widget value with session state

st.subheader("Initialize widget value with session state")

# Callbacks
st.subheader("Use callbacks")

st.markdown("#### Select your time range")

st.radio("Select a range", ["7 days", "28 days", "custom"], horizontal=True)

col1, col2, col3 = st.columns(3)

col1.date_input("Start date")
col2.date_input("End date")
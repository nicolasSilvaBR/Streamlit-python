import streamlit as st

st.title("Stateful apps")

st.write("Here is the session state:")
st.write(st.session_state)
st.button("Update state")

# Set the value using the key-value syntax
if "key" not in st.session_state:
    st.session_state["Key"] = "Value"

maxDate = '2024-04-01'

# Set the value using the attribute syntax
if "MinDate" not in st.session_state:
    st.session_state.MinDate = "2024-09-20"  

if "MaxDate" not in st.session_state:
    st.session_state.MaxDate = maxDate

# Read value from session stat
st.session_state["MinDate"]
st.session_state["MaxDate"]

# Update values in state
st.session_state["MinDate"] = '2024-01-01'

# Delete item in state
del st.session_state["MinDate"]

st.divider()

st.date_input(label="Start Date",key="MinDate")

minDate = st.session_state["MinDate"]

st.session_state["MinDate"]
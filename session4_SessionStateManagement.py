# Session State Management
# Allow us to share variable between runs for each session
# The session state persists values across runs for a single session
# The cache persists values across runs and sessions
# State: affects a single user in a single session
# cache: affects all users across all sessions and runs

import streamlit as st

st.title("Stateful apps")

st.write("Here is the session state:")
st.write(st.session_state)
st.button("Update state")

# Set the value using the key-value syntax


# Set the value using the attribute syntax


# Read value from session state


# Update values in state


# Delete item in state
 
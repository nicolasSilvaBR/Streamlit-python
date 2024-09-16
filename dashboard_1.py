import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

URL = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"

df = pd.read_csv(URL, dtype={'Quarter': str, 
                            'Canada': np.int32,
                            'Newfoundland and Labrador': np.int32,
                            'Prince Edward Island': np.int32,
                            'Nova Scotia': np.int32,
                            'New Brunswick': np.int32,
                            'Quebec': np.int32,
                            'Ontario': np.int32,
                            'Manitoba': np.int32,
                            'Saskatchewan': np.int32,
                            'Alberta': np.int32,
                            'British Columbia': np.int32,
                            'Yukon': np.int32,
                            'Northwest Territories': np.int32,
                            'Nunavut': np.int32})

st.title("Population of Canada")
st.write("Source table can be found [here](https://discuss.streamlit.io/t/hyperlink-in-streamlit-without-markdown/7046/3)")

# Show full table with expander
df["Q"] = df["Quarter"].str[0:2]
df["Year"] = df["Quarter"].str[2:].astype(int)
minYear = int(df["Year"].min())
maxYear = int(df["Year"].max())

with st.expander("See full table"):
    st.write(df)    

# create a form 
with st.form("form_key"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Choose a starting date")
        startQuarter = st.selectbox(label="Start Quarter", options=df["Q"].sort_values().unique())  
        sliderMinYear = st.slider(label="Start Year",min_value=minYear,max_value=maxYear,step=1,value=minYear)    

    with col2:
        st.write("Choose an end date")
        endQuarter = st.selectbox(label="End Quarter", options=df["Q"].sort_values().unique())
        sliderMaxYear = st.slider(label="Start Year",min_value=minYear,max_value=maxYear,step=1,value=maxYear)

    with col3:
        st.write("Choose a location")
        location = st.selectbox(label="Location", options=df.columns[1:].sort_values().unique())

    submitBtn = st.form_submit_button(label="Submit",type="primary")
    
    startQuarter
    endQuarter
    sliderMinYear
    sliderMaxYear
    location    
    
tab1, tab2 = st.tabs(["Population Change","Compare"])

# Filter the Year First

#df = df[ df["Year"]>=sliderMinYear & df["Year"]<=sliderMaxYear ]
#df.loc[(df["Year"] >= sliderMinYear) & (df["Year"] <= sliderMaxYear) & (df["Quarter"] >= startQuarter & (df["Quarter"] <= endQuarter))]



with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.write("Column1")
    with col2:
        #  Y = Pupulation X = Time series
        #st.line_chart(df,x="Population")
        st.write("Column1")
with tab2:
    st.write("tab2")

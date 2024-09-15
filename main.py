import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime


# Text Elements
# App title
st.title("Reports")
# Header
st.header("st.header")
# Subheader
st.subheader("st.header")
# Markdown
st.markdown("# st.header")
# Caption
st.caption("st.header")
# Code block
st.code("import sreamlit as st")
# Preformatted text
st.text("Some text")
# LaTeX
st.latex("x = x ** 2")
# Divider
st.write("Write")
st.divider()
#st.write


# Data Sources
datasource = pd.read_csv("data/sample.csv")
datasource_map = pd.read_csv("data/sample_map.csv")


# Data Display Elements
st.dataframe(datasource)
st.write(datasource)
st.metric(label = 'Metric KPI',value=900,delta=20,delta_color='normal')
st.metric(label = 'Metric KPI',value=900,delta=20,delta_color='inverse')


# Charting Elements


# Streamlit line chart
st.line_chart(datasource,x='year',y=["col1","col2","col3"])
# Streamlit area chart
st.area_chart(datasource,x='year',y=["col1","col2","col3"])
# Streamlit bar chart ( by Default is stacked )
st.bar_chart(datasource,x='year',y=["col1","col2","col3"])
# Streamlit map
st.map(datasource_map,latitude='latitude',longitude='longitude')
# Matplotlib
fig, ax = plt.subplots()
ax.plot(datasource.year, datasource.col1)
ax.set_title("My figure title")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate()
st.pyplot(fig)


# Input Widgets - Part 1


# buttons
primaryButton = st.button("Primary",type="primary")
secondaryButton = st.button("Seconday",type="secondary")
if primaryButton:
    st.write("primary Button")
if secondaryButton:
    st.write("secondary Button")
# Checkbox
checkbox = st.checkbox(label="Remenber me")
if checkbox:
    st.write("I Will remember you !")
else:
    st.write("I Will NOT remember you !")


# Radio buttons
radio = st.radio(label="Choose a column",options=datasource.columns[1:],index=0,horizontal=True)
if radio:
    st.write(f"You choose : {radio}")
# Selectbox
selectbox = st.selectbox(label="Select box",options=datasource.columns[1:],index=0,placeholder="nao entendi",help="Choose a option from the dropdow")
if selectbox:
    st.write(f"You choose : {selectbox}")


# Multiselect
Multiselect = st.multiselect(label="MultiSelected",options=datasource.columns[1:],default=["col1","col2"])
st.write(Multiselect)


# Slider
st.slider(label="Slider",min_value=0,max_value=10,step=1,value=5)
# Text input
Textinput = st.text_input(label="Text Input",value=None,placeholder="Type Something")
st.write(Textinput)
# Number input
st.number_input(label="Number Input",min_value=0,max_value=10,value=5)
# Text Area
st.text_area(label="Text Area",height=200,placeholder="Type here")
# Date Input
st.divider()


col1, col2 = st.columns(2)
today = datetime.datetime.today()
yesterday = (today - datetime.timedelta(days=1)).strftime("%d-%m-%Y")


options ={"Today":today,"Yesterday":yesterday}


with col1:    
    selectedDate = st.selectbox(label="Date Picker",options=options)
    options[selectedDate]
with col2:
    date = st.date_input(label="Date",value="today",format="DD/MM/YYYY")
    options[selectedDate]


st.divider()
# Time input
st.time_input(label="Time")


st.divider()
# Forms MUST have form_key
with st.form("form_key"):
    st.write("Forms")
    submit_btn = st.form_submit_button("Submit")


# Layout
# Sidebar
with st.sidebar:
    st.write("Some code")
# Columns
col1, col2, col3 = st.columns(3)
col1.write("Column 1")
col2.write("Column 2")
col3.write("Column 3")
st.divider()


# Tabs
tab1, tab2 = st.tabs(["Line Chart","Bar Chart"])
df = pd.read_csv("data/sample.csv")
with tab1:
    linechart = st.line_chart(df,x='year',y=["col1","col2","col3"])
with tab2:    
    barchart = st.bar_chart(df,x='year',y=["col1","col2","col3"])


# Expander
with st.expander("Expander",icon="🚨"):
    st.write("Something here")
# Container


with st.container():
    st.write("Inside a container")






import streamlit as st
import pandas as pd
import numpy as np
st.title("My First Streamlit App") ## This line sets the title of the app
st.write("Hello, welcome to my first Streamlit app!") ## This line writes a welcome message to the app
 
# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data) ## This line creates a DataFrame using the pandas library
st.write("Here is a simple DataFrame:") ## This line writes a message to the app
st.dataframe(df) ## This line displays the DataFrame in the app

# Create a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']     
)
st.line_chart(chart_data) ## This line creates a line chart using the random data generated above
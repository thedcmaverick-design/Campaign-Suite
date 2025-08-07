import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Campaign Dashboard", layout="wide")

st.title("📊 Campaign Finance Dashboard")
st.write("Track fundraising across races in real time.")

# Example CSV — replace with your own file
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Race': ['Race A', 'Race B', 'Race C'],
        'Candidate': ['Alice', 'Bob', 'Charlie'],
        'Funds Raised': [50000, 30000, 45000]
    })
    return data

df = load_data()

# Show table
st.dataframe(df)

# Plot
fig = px.bar(df, x="Candidate", y="Funds Raised", color="Race",
             title="Funds Raised by Candidate")
st.plotly_chart(fig, use_container_width=True)

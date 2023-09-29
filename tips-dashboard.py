# importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Tips Dashboard",
                   page_icon=None, 
                   layout="wide", 
                   initial_sidebar_state="expanded")

# loading data
df = pd.read_csv('tips.csv')

# sidebar
st.sidebar.header("Tips Dashboard")
st.sidebar.image('tips.jpg')
st.sidebar.write("This dashboard is using Tips dataset from seaborn for educational purposes.")
st.sidebar.write("")
st.sidebar.write("Filter your data:")
cat_filter = st.sidebar.selectbox("Categorical Filtering",[None,'sex','smoker','day','time'])
num_filter = st.sidebar.selectbox("Numerical Filtering",[None,'total_bill','tip'])
row_filter = st.sidebar.selectbox("Row Filtering",[None,'sex','smoker','day','time'])
col_filter = st.sidebar.selectbox("Column Filtering",[None,'sex','smoker','day','time'])
st.sidebar.write("")
st.sidebar.markdown("Made with :heart_eyes: by Eng. [Mustafa Othman](https://www.youtube.com/c/MustafaOthman/)")


# body

# row a
a1, a2, a3, a4 = st.columns(4)

a1.metric("Max. Total Bill", df['total_bill'].max())
a2.metric("Max. Tip", df['tip'].max())
a3.metric("Min. Total Bill", df['total_bill'].min())
a4.metric("Min. Tip", df['tip'].min())

# row b
st.subheader("Total Bills vs. Tips")
fig = px.scatter(data_frame=df, 
                 x='total_bill',
                 y='tip',
                 color=cat_filter,
                 size=num_filter,
                 facet_col=col_filter,
                 facet_row=row_filter)
st.plotly_chart(fig, use_container_width=True)

# row c
c1, c2, c3 = st.columns((4,3,3))

with c1:
    st.text("Sex vs. Total Bills")
    fig = px.bar(data_frame=df, x='sex', y='total_bill', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.text("Somker/Non-smoker vs. Tips")
    fig = px.pie(data_frame=df, names='smoker', values='tip', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.text("Days vs. Tips")
    fig = px.pie(data_frame=df, 
                 names='day', 
                 values='tip', 
                 color=cat_filter,
                 hole=0.4)
    st.plotly_chart(fig, use_container_width=True)
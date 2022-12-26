import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
st.title('My portfolio site')
col1,col2=st.columns(2)

with col1:

    st.image('images/photo.jpg',use_column_width='auto')

with col2:

    st.title('Milan Kricka')

    content="""Electrical Engineer with a demonstrated history of working in the information technology and services 
    industry. Certified IBM Data Analyst. Strong engineering professional with high analytical skills, devoted 
    to grow in field of Business Intelligence and Analysis. Devoted, disciplined, resourceful, creative and
     adaptable. Oriented toward using sustainable technology solutions. """
    st.info(content)

content2="""some text 

"""

st.write(content2)

df=pd.read_csv("data.csv",sep=';')

col3,empty_col,col4=st.columns([1.5,0.5,1.5])

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code]({row['url']})")




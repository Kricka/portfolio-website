import streamlit as st

st.set_page_config(layout='wide')

col1,col2=st.columns(2)

with col1:

    st.image('images/photo.jpg',width=300)

with col2:

    st.title('Milan Kricka')

    content="""Electrical Engineer with a demonstrated history of working in the information technology and services 
    industry. Certified IBM Data Analyst. Strong engineering professional with high analytical skills, devoted 
    to grow in field of Business Intelligence and Analysis. Devoted, disciplined, resourceful, creative and
     adaptable. Oriented toward using sustainable technology solutions. """
    st.info(content)

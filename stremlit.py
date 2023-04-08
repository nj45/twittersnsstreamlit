import streamlit as st
st.title('Twitter scraping Dashboard')
text= st.text_input('Query')
since = st.date_input('Since')
until = st.date_input('Until')
count = st.number_input('count')
submit = st.button('GO')
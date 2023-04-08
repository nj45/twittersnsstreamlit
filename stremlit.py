import streamlit as st 
from twitter import tweets
# adding a title
st.title('Twitter scraping Dashboard')
 
  
#fetching inputs


text= st.text_input('Query')
since = st.date_input('Since')
until = st.date_input('Until')
count = st.number_input('count')
# submit button
submit = st.button('GO')

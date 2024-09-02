import streamlit as st
st.title('MY first app')
st.write('Hello all')
x=st.text_input('which technology you want to learn?')
if x=='Ai':
    st.write('kindly enroll in python first.')
y=st.radio('are you graduate?',options=['Yes','No'])
if y=='Yes':
    st.write('you can enroll in our diploma course.')
else:
    st.write('you can do internship.')
a=st.button('show')
if a==1:
    st.write('u r cute.')

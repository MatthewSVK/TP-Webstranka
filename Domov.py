import streamlit as st

st.header('Zápisnice zo stretnutí')
st.subheader('Zápisnica 1')
with open('zapisnice/zapisnica1.txt', 'r') as file:
    zapis1 = file.read()
st.download_button('Stiahnuť zápisnicu', data=zapis1, file_name='zapisnica1.txt', mime='text/plain')

with open('zapisnice/zapisnica2.txt', 'r') as file:
    zapis1 = file.read()
st.download_button('Stiahnuť zápisnicu', data=zapis1, file_name='zapisnica2.txt', mime='text/plain')
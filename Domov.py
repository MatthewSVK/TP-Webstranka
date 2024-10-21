import streamlit as st

st.header('Zápisnice zo stretnutí')
st.subheader('Zápisnica 1')
with open('zapisnice/TP_Zapisnica1.pdf', 'rb') as file:
    zapis1 = file.read()
st.download_button('Stiahnuť zápisnicu', data=zapis1, file_name='TP_Zapisnica1.pdf', mime='application/octet-stream')

st.subheader('Zápisnica 2')
with open('zapisnice/TP_Zapisnica2.pdf', 'rb') as file:
    zapis2 = file.read()
st.download_button('Stiahnuť zápisnicu', data=zapis2, file_name='TP_Zapisnica2.pdf', mime='application/octet-stream')

st.subheader('Zápisnica 3')
with open('zapisnice/TP_Zapisnica3.pdf', 'rb') as file:
    zapis3 = file.read()
st.download_button('Stiahnuť zápisnicu', data=zapis3, file_name='TP_Zapisnica3.pdf', mime='application/octet-stream')
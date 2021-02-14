import streamlit as st
import pandas as pd
import numpy as np
import requests
from urllib.parse import urljoin


# variables for api calls
url = "http://127.0.0.1:8000"
files = None


#setting up the colours
st.markdown("""
<style>
body {
    color: ;
    background-color: white;
}
</style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>CRSAS</h1>", unsafe_allow_html=True)

st.subheader('Upload Files to see the review')

uploaded_file = st.file_uploader("Upload Files",type=['wav'])


@st.cache(suppress_st_warning=True)
def fileUpload():
    if uploaded_file is not None:
        files = {'files': uploaded_file}

        response = requests.request("POST", urljoin(url, '/voice/'), files=files)
        if response.json() !=  None: 
            st.markdown("<h3>Text Spoken</h3>\
            {text},\
            <h3> Sentiment</h3>\
            {cls}".format(text = response.json()['text'], cls = response.json()['cls']), unsafe_allow_html=True)

if st.button('Predict'):
    fileUpload()

#get info from the database
@st.cache(suppress_st_warning=True)
def getData():
    response = requests.request("GET", urljoin(url, '/data/'))
    if response.json() !=  None:
        output = list(response.json().values())
        text = [o['text'] for o in output[0]]
        classification = [o['cls'] for o in output[0]]
        df = pd.DataFrame({'text': text, 'cls': classification})
        st.write(df)

if st.button("Get Database"):
    getData()

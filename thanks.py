import streamlit as st

import requests
from streamlit_lottie import st_lottie
import json

st.markdown("""
# BucePy 🦖

De un teórico, para los teóricos.
""")

hide_st_style="""
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header('Email enviado! 📧')
st.subheader('Gracias por contribuir!')
st.write("Aqui puedes volver a [BucePy](https://bucepythanks.streamlit.app/) .")

def load_lottiefile(filepath:str):
    with open(filepath,'r') as f:
        return json.load(f)


def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_email=load_lottiefile('Lottie/emailsent.json')
st_lottie(lottie_email,height=400,width=400)
def read_css(file_name):
        with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
read_css('style/style.css')

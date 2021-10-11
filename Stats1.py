import streamlit as st
#import pandas as pd
import numpy as np
from time import sleep
import time

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)   #removed hamburger menu

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True) # removes padding


st.markdown("## Party time!")
st.write("Yay! you have took 1st step to learn. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()

st.title("Welcome to abslute Basics")

dataframe = np.random.randn(10,1 )
st.write('## mean = ',np.mean(dataframe))
st.write('## median = ',np.median(dataframe))
#st.write('mode = ',np.m(dataframe))
st.dataframe(dataframe)

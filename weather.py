import streamlit as st
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.header('Weather Tracker')

st.write('Enter a City here to check weather')
user_input = st.text_input("", "Tokyo")

# enter city name
city = user_input
# create url
url = "https://www.google.com/search?q="+"weather"+city
# requests instance
html = requests.get(url).content
# getting raw data
soup = BeautifulSoup(html, 'html.parser')
# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split('\n')
time = data[0]
sky = data[1]
   
# list having all div tags having particular class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
   
# particular list with required data
strd = listdiv[5].text
   
# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]

st.write("Temperature is", temp)
st.write("Time: ", time)
st.write("Sky Description: ", sky)
st.write('Other Data: ', other_data)

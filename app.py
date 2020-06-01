import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webbrowser as wb

st.title("Heart Disease Prediction!")
st.header("A person may or may not suffer from heart disease in future can be predicted")

data = pd.read_csv("D:\Desktop\heart.csv")
x = data['chol']
y = data['trestbps']
z = data['age']
df = pd.DataFrame({
      'age':[22,34,54,75,34,64,38,43]})

if st.checkbox("Visualize Cholestrol level"):
      fig = plt.figure()
      plt.hist(x, bins  = 20)
      st.pyplot(fig)

if st.checkbox("Visualize Blood Pressure level"):
      st.line_chart(y)

if st.checkbox("World Map"):
      st.map()

options  = st.sidebar.selectbox("What is your age?",z)
ages = st.selectbox("Whats your age?",df['age'])
slide = st.slider('slide',20,80)

if  st.checkbox("Show Raw Data"):
      st.subheader("Raw Data")
      st.write(data)

url = 'https://www.ashuhacks.tech/'
if st.button('Our Website'):
      wb.open_new_tab(url)


         
      

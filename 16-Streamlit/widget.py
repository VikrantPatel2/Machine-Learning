import streamlit as st
import pandas as pd

st.title("Streamlit Text Input Widget")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:",0,100,25)

st.write(f"Your name is {name} and you are {age} years old.")

options=["Select Language","Python","Java","C++","JavaScript"]
choice=st.selectbox("Choose  Your Favorite language:",options)
st.write(f"You selected: {choice}.")
if name:
    st.write(f"Hello, {name}!")

data={
    "Name":["John","Jack","Alice","Bob"],
    "Age":[30,25,28,22],
    "City":["New York","Los Angeles","Chicago","Houston"]
}
df=pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploded_file=st.file_uploader("Choose a CSV file",type="csv")
if uploded_file is not None:
    df=pd.read_csv(uploded_file)
    st.write(df)
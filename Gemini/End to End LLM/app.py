# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:42:09 2023

@author: abhishek anilkumar
"""

# Importing the necessary modules for configuration and execution
from dotenv import load_dotenv  # Loading environment variables from a .env file
load_dotenv()  # Executing the process to load all environment variables

import streamlit as st  # Importing the Streamlit library for creating interactive web applications
import os  # Importing the os module for interacting with the operating system

# Importing the Google Generative AI module for specific functionalities
import google.generativeai as genai  # Note: Please ensure the correct module path based on your project structure


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini model and get responses
model=genai.GenerativeModel('gemini-pro')
def get_gemini_res(prompt):
    response=model.generate_content(prompt)
    return response.text


# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Demo")  # Set the page title for the Streamlit app
st.header("Gemini Pro Text Prompt Application")  # Display a header for the Streamlit app
input_text = st.text_input("Input: ", key="input")  # Create a text input widget for user input, with a specified key
submit_button = st.button("Gemini Pro here to help you!")  # Create a button labeled "Gemini Pro here to help you!"

if submit_button:
    # Retrieve the Gemini response based on the user input
    response = get_gemini_res(input_text)

    # Display the response as a subheader and write it to the Streamlit app
    st.subheader("Certainly! The Response is")
    st.write(response)

    
    
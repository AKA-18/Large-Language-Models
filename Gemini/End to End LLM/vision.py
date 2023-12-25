# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:11:06 2023

@author: abhishek anilkumar
"""

# Importing the necessary modules for configuration and execution
from dotenv import load_dotenv  # Loading environment variables from a .env file
load_dotenv()  # Executing the process to load all environment variables

import streamlit as st  # Importing the Streamlit library for creating interactive web applications
import os  # Importing the os module for interacting with the operating system

# Importing the Google Generative AI module for specific functionalities
import google.generativeai as genai  # Note: Please ensure the correct module path based on your project structure

from PIL import Image  # Importing the Image module from the Python Imaging Library (PIL)

# Configure the Google Generative AI module
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create an instance of the Gemini Pro Vision model
model = genai.GenerativeModel('gemini-pro-vision')

# Function to load gemini model and get responses
def get_gemini_res(input, image):
    """
    Get response from the Gemini Pro Vision model based on input and/or image.

    Parameters:
    - input (str): The input text prompt.
    - image (str or PIL.Image): The image input for the model.

    Returns:
    - str: The generated response text from the Gemini Pro Vision model.
    """
    # Check if there is input text provided
    if input != "":
        # Generate content using both input text and image
        response = model.generate_content([input, image])
    else:
        # Generate content using only the image
        response = model.generate_content(image)

    # Extract and return the generated response text
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Text-Image Demo")  # Set the page title for the Streamlit app
st.header("Gemini Vision Pro Image Text Prompt Application")  # Display a header for the Streamlit app

# Create a text input widget for user input prompt
input_text = st.text_input("Input Prompt: ", key="input")

# Allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

# Display the uploaded image if available
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Create a button labeled "Tell me about the image"
submit_button = st.button("Tell me about the image")

# If the "Tell me about the image" button is clicked
if submit_button:
    # Get the Gemini response based on the input prompt and uploaded image
    response = get_gemini_res(input_text, image)
    
    # Display the response as a subheader and write it to the Streamlit app
    st.subheader("The Response is")
    st.write(response)

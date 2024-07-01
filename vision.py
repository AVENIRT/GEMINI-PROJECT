from dotenv import load_dotenv
load_dotenv() ##### load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

###### function to load gemini model and gemini pro model and get response
model=genai.GenerativeModel('gemeni-pro-vision')
def get_gemini_response(input,image):

    if input!='':
        response=model.generate_content([input,image])
    else: 
        response=model.generate_content(image)
    return response.text

###### initialize our streamlit app

st.set_page_config(page_title='Gemini image demo')

st.header('Gemini Application')

##### some infos , I am specically give
inpiut=st.text_input('Input Prompt: ', key='input')

### create image upload option

uploaded_file=st.file_uploader("choose image...", type=['jpg','jpeg','png'])
image=''
if uploaded_fileis not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)


#### know about the image

submit=st.button('Tell about the image')

##### if submit is clicked

if submit:

    response=get_gemini_response(input,image) #### Get the method

    st.subheader('the response is')
    st.write(response)


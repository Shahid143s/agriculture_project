import streamlit as st
import numpy as np
from button import styled_button1_html
from button import styled_button2_html
from button import styled_container_css
from button import css
from button import css2
import time

st.title("Academic Internship Project")
st.subheader("Use of Machine Learning in Agriculture")

# Sidebar-------------------------------------
# Sidebar content
with st.sidebar:
    st.title("Team Members")

    # Create two columns
    col1, col2 = st.columns(2)

    # Define member information
    members = [
        {"name": "Shahid Anowar", "img_url": "https://i.ibb.co/6m9Gt2s/IMG20231128135521-modified.png"},
        {"name": "Joyosmita Paul", "img_url": "https://i.ibb.co/nmJkh8K/Whats-App-Image-2024-07-16-at-7-47-30-PM-modified.png"},
        {"name": "Abhisekh Pandit", "img_url": "https://i.ibb.co/vvz18jp/Whats-App-Image-2024-07-16-at-2-24-20-PM-modified.png"},
        {"name": "Prem Kr Sah", "img_url": "https://i.ibb.co/935nGLT/imageedit-1-7430777653-modified.png"},
        {"name": "Manas Seal", "img_url": "https://i.ibb.co/Y30fxQ7/IMG-20240715-173204-modified.png"}
    ]
#https://i.ibb.co/qjNqCwF/Picsart-24-07-16-13-37-07-577.png
    # Add members to columns
    for i, member in enumerate(members):
        col = col1 if i % 2 == 0 else col2
        col.markdown(f'''
        <div class="circle-bordered-container2">
            <img src='{member["img_url"]}' alt='Image'>
        </div>
        <p style='text-align:center;'>{member["name"]}</p>
        ''', unsafe_allow_html=True) 
    

st.markdown(styled_container_css, unsafe_allow_html=True)
#--Spinner Bar--
with st.spinner('Loading Tools'):
    time.sleep(2)
success_placeholder = st.empty()

# Columns-------------------------------------
col1, col2 = st.columns(2)
st.markdown(css, unsafe_allow_html=True)
# Column 1
with col1:
    st.markdown('''<div style='text-align:center;' class="bordered-container">
                    <h3>Crop Recommendation System</h3>
                    <img src='https://media.licdn.com/dms/image/D5612AQEx2AMyErNfxQ/article-cover_image-shrink_600_2000/0/1710648344420?e=2147483647&v=beta&t=5E0GoftZHK9Bz81pwUehZ0YveQ0vwS7pHxzZKIJepwk' alt='Image' style='width:300px;height:200px;' caption="Column 2 Image">
                    <figcaption>A Crop Recommendation System leverages soil data and climate conditions to suggest optimal crops for farmers, enhancing yield, sustainability, and profitability with data-driven agricultural practices.</figcaption>
                    </div>
                ''', unsafe_allow_html=True)
    st.markdown(styled_button1_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    

# Column 2
with col2:
    st.markdown('''<div style='text-align:center;' class="bordered-container">
                    <h3>Plant Disease Classifier <br></h3>
                    <img src='https://i.ytimg.com/vi/zcq5aw9t-Ds/maxresdefault.jpg' alt='Image' style='width:300px;height:200px;' caption="Column 2 Image">
                    <figcaption>The Plant Disease Classifier uses advanced machine learning to accurately identify plant diseases from images, providing crucial early detection and facilitating timely, effective treatment for healthier crops.</figcaption>
                    </div>
                ''', unsafe_allow_html=True)
    st.markdown(styled_button2_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    


success_placeholder.success('Tools loaded!')
time.sleep(2)
success_placeholder.empty()
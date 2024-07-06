# make background remover app and user can upload image and remove background
# make model using 
# use streamlit to make app

import streamlit as st
import requests
import os
from PIL import Image
from io import BytesIO

# set title
st.title('Background Remover App')

# upload image
image = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

# check if image is uploaded
if image:
    # display image
    img = Image.open(image)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # remove background
    if st.button('Remove Background'):
       
    
    

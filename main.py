import PIL.Image
import streamlit as st
from gemini_helper import read_image
from playsound import playsound

st.title("Image Reader 📸")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)
    st.image(img, use_column_width=True)
    st.write("")

    with st.spinner("Image Detection In Progress..."):
        image_description = read_image(img)

    st.write("Image Description :")
    st.write(image_description)

    playsound('description.mp3')


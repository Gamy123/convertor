import streamlit as st
from PIL import Image
from io import BytesIO

st.title("Image converter JPG,PNG,JPEG")

img_up = st.file_uploader('Upload a PNG or JPG image', type=['png', 'jpg', 'jpeg'])
col1, col2 = st.columns(2)
try:
    if img_up:
        image = Image.open(img_up)
        org_image = Image.open(img_up)
except:
    st.error('File is corrupted.')
try:
    if img_up.type == "image/png":
        convert_button = st.empty()
        if convert_button.button("Convert to JPG"):
            image = image.convert('RGB')
            with col2:
                st.image(image, caption='Converted to JPG')
                image_bytes = BytesIO()
                image.save(image_bytes, format='JPEG')
                st.download_button(
                    label="Download image",
                    data=image_bytes.getvalue(),
                    file_name="image.jpg",
                    mime="image/jpeg"
                )
            with col1:
                st.image(org_image, caption='Uploaded Image')
            convert_button.empty()

    else:
        convert_button = st.empty()
        if convert_button.button("Convert to PNG"):
            image = image.convert('RGB')
            with col2:
                st.image(image, caption='Converted to PNG')
                image_bytes = BytesIO()
                image.save(image_bytes, format='PNG')
                st.download_button(
                    label="Download image",
                    data=image_bytes.getvalue(),
                    file_name="image.png",
                    mime="image/png"
                )
            with col1:
                st.image(org_image, caption='Uploaded Image')
            convert_button.empty()
except:
    st.error('Something went wrong please try again')

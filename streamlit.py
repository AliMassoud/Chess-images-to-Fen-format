import requests
import streamlit as st
from PIL import Image

# def app():
st.subheader("AI Chess")
data_file = st.file_uploader("Upload image", type=['.jpg', '.png', '.jpeg'])
if st.button("Process"):
    if data_file is not None :
        file = {"image": data_file}
        # st.image(open(file['image']))
        res = requests.post(f"http://127.0.0.1:5000/SubmitFile", files=file)
        st.image(data_file)
        st.write(res.json()['msg'])
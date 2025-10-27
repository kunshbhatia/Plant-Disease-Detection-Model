import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0" # To remvoe the errors of tensorflow

import streamlit as st
import random
from backend_prediction import prediction_plant

st.set_page_config(page_title="Plant Disease Detection",
                   page_icon= "🌿", layout="wide",initial_sidebar_state="expanded")

hide_github_icon = """
<style>
#GithubIcon {
    visibility: hidden;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
 
st.header("Plant Disease Detector 🌿")

# Uploading the file and a submit button

file_uploaded = st.file_uploader("Upload Image of Plant's Leaf",accept_multiple_files=False,type=[".jpg","jfif",".png"])

image_one = "examples/CornCommonRust1.JPG" # For sample images
image_second = "examples/TomatoHealthy1.JPG"
image_third = "examples/TomatoYellowCurlVirus3.JPG"

with st.expander("Sample Images"):
    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        st.image(image_one,width=150)
        st.text("Corn Common Rust")
        first_submit = st.button("Select",key="First_image")

    with col2:
        st.image(image_second,width=150)
        st.text("Tomato Healthy")
        second_submit = st.button("Select",key="Second_Image")

    with col3:
        st.image(image_third,width=150)
        st.text("Tomato Yellow Curl Virus")
        third_submit = st.button("Select",key="Third_Image")
        
    with col2:
        if first_submit:
            st.session_state["selected_image"] = image_one  # st.session_state :- Saves a varibale across the whole script
            st.success("First Image Selected")
        elif second_submit:
            st.session_state["selected_image"] = image_second
            st.success("Second Image Selected")
        elif third_submit:
            st.session_state["selected_image"] = image_third
            st.success("Third Image Selected")

selected_image = st.session_state.get("selected_image", None)

submitted = st.button("Submit",key="Submit_Button")

# Creating Sidebar
class_list = ["Apple","Blueberry","Corn","Cherry","Grape" ,"Orange","Peach","Pepper","Potato","Raspberry","Soyabean","Strawberry","Tomato"]
st.sidebar.title("Plants Whose Disease Model Can Detect") 
for i in class_list:
        st.sidebar.text(f"- {i}")

if submitted:

    if file_uploaded:
        image_to_use = file_uploaded
    elif selected_image:
        image_to_use = selected_image
    else:
        st.error("Please upload or select an image first!")
        st.stop()

    col1, col2 = st.columns([1, 1])

    with col1:
        if file_uploaded:
            st.image(file_uploaded, width=350)
        elif selected_image:
            st.image(selected_image, width=350)

    with col2:
        # Run prediction
        emoji = ["😁","😃","🥰","😙","🥳","😇","🤭","🙈","🦚","👀"]
        with st.spinner(f'Predicting , Please Wait {random.choice(emoji)} '):
            final_prediction_disease = prediction_plant(image_to_use)

        # Green box for prediction result
        st.markdown(
        f"""
        <div style="
            margin: 75px auto;
            width: 100%;
            background: linear-gradient(145deg, #eafaf1, #d6f5df);
            border-left: 8px solid #2E8B57;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #155724;
            box-shadow: 0 4px 20px rgba(46,139,87,0.25);
            letter-spacing: 1px;
        ">
             <span style="font-size:26px;">{final_prediction_disease}</span>
            <p style="font-size:16px; color:#2E8B57; margin-top:8px;">— Plant Health Status —</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def warning(): # Used to have images in explander below
    col1,col2 = st.columns([1,1])

    with col1:
        st.image("examples/AppleScab3.JPG",width=200)
        st.error("NOT TO USE")
 
    with col2:
        st.image("examples/TomatoEarlyBlight4.JPG",width=200)
        st.success("PERFECT TO USE")

    return " "


with st.expander("How to get ACCURATE Result 💯"): 
                st.markdown(f""" 
                    - Make sure the uploaded image is a picture of a leaf.
                    - Ensure the leaf has a background color that is different with it, so the model can detect it easily. 
                    - {warning()}Ensure that the image of the leaf fits the frame .
                    - Do NOT use bulrry or very much filtered image. 
                    """)

st.markdown("""<p style="margin-top: 40px; text-align: center; color: gray;">
  © 2025 Kunsh Bhatia | Built with ❤️ and ☕
</p>
""", unsafe_allow_html=True)

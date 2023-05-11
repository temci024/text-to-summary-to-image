import streamlit as st
from utils import summarize,generate_image

st.title("Text to summar to image")
st.header("This is a sample web app that summarizes text and generates an image of the summary")


text = st.text_area("Enter your text below","Astronaut riding a bicycle in the beach")

if st.button("Summarize and Generate Image"):
    if not text:
        st.error("please input a text in the text box")
    else:
        with st.spinner("Summarizing...."):
            summary = summarize(text)

        with st.spinner("Generating Image......"):
            image = generate_image(summary)

        st.info(f"Summary: {summary}")
        st.image(image)

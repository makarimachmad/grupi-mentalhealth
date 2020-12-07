import streamlit as st
from PIL import Image


def home_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )

    image = Image.open('././sources/img/cover.jpg')
    st.image(image, caption='via Unsplash - Tim Mossholder', use_column_width=True)
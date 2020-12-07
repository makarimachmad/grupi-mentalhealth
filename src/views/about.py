import pathlib
import utils.display as udisp

import streamlit as st

def write():
    #udisp.title_awesome("About")

    st.title('Credits')
    udisp.render_md("sources/credits.md")
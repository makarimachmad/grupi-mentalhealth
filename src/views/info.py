import pathlib
import utils.display as udisp

import streamlit as st
import core.infographic.info as info

def write():
    #udisp.title_awesome("Infographic Tweet")
    st.title('Infographic Tweet')
    info.info_main("Infographic","coba")

import pathlib
import utils.display as udisp

import streamlit as st
import core.home.home as hm


def write():
    #udisp.title_awesome("Mental Health Solver")
    hm.home_main("Home","Home")
    udisp.render_md("sources/home_info.md")


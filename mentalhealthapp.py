import streamlit as st

import utils.display as udisp

import src.views.home
import src.views.about
import src.views.nlp
import src.views.info

MENU = {
    "Home" : src.views.home,
    "Analyzer" : src.views.nlp,
    "Infographics" : src.views.info,
    "Credits" : src.views.about
}

def main():
    st.sidebar.title("Mental Health Humanity")
    menu_selection = st.sidebar.radio("Choice your option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

    st.sidebar.info(
        "demoapps/HealthHumanityApp"
    )

if __name__ == "__main__":
    main()
import pathlib
import utils.display as udisp

import streamlit as st
import core.nlp.sentimen as rf

def write():
    #udisp.title_awesome("Mental Health Sentiment Analyzer")
    st.title('Tweet Sentiment Analyzer')
    rf.nlp_main("NLP", "Review Tweets")

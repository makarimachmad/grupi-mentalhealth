import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt


def info_main(title, subtitle):
    st.sidebar.title(title)
    st.sidebar.info(
        subtitle
    )

    chart_data = pd.read_csv('././sources/data_twit.csv')
    chart_data = chart_data.rename(columns={'date':'index'}).set_index('index')
    st.line_chart(chart_data)

    DATE_COLUMN = 'date/time'
    DATA_URL = ('././sources/uber-raw-data-sep14.csv')

    @st.cache
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache)")

    # chart_data = pd.DataFrame(
    #      np.random.randn(20, 3),
    #      columns=['pand_all', 'bos_all', 'cemas_all','depresi_all','stres_all'])


    histo_data = pd.read_csv('././sources/total.csv')
    st.subheader('Jumlah Data Per Keyword')
    #hist_values = np.histogram(histo_data.set_index('keyword'))
    histo_data = histo_data.rename(columns={'keyword':'index'}).set_index('index')
    st.bar_chart(histo_data)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    # st.subheader('Jumlah Data Per Kategori')
    # hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    # st.bar_chart(hist_values)

    # Some number in the range 0-23
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader('Map of all tweets at %s:00' % hour_to_filter)
    st.map(filtered_data)
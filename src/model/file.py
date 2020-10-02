""" Load data from file """

import pandas as pd
import streamlit as st


@st.cache(show_spinner=False)
def load_data():
    """ Function to load data from file and persist on cache """
    return pd.read_parquet("data/filtered_dh_survey.parquet")

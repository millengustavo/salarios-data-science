import pandas as pd
import streamlit as st


@st.cache(show_spinner=False)
def load_data():
    return pd.read_parquet("data/filtered_dh_survey.parquet")

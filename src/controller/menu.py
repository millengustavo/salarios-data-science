import streamlit as st
import pandas as pd


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df = _select_degree_level(df)
    df = _select_time_experience_data_science(df)
    df = _select_job_situation(df)
    df = _select_most_used_programing_languages(df)
    # df = _select_time_experience_before(df)
    # df = _select_is_data_science_professional(df)
    # df = _select_online_courses(df)
    # df = _select_is_manager(df)
    # df = _select_anonymized_degree_area(df)
    # df = _select_anonymized_market_sector(df)
    # df = _select_anonymized_role(df)
    # df = _select_anonymized_manager_role(df)

    return df


def _select_degree_level(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('P8', 'degreee_level')", 
     "Escolaridade")


def _select_time_experience_data_science(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df, 
    "('P17', 'time_experience_data_science')",
     "Tempo de Experiência com Data Science")


def _select_time_experience_before(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df, 
    "('P18', 'time_experience_before')", 
    "Tempo de experiência anterior na área de TI/Engenharia de Software")


def _select_job_situation(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df, 
    "('P10', 'job_situation')", 
    "Situação atual de trabalho")


def _select_is_data_science_professional(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('P19', 'is_data_science_professional')", 
     "Profissional de Data Science")


def _select_most_used_programing_languages(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('P22', 'most_used_proggraming_languages')", 
     "Linguagem de Programação mais utilizada")


def _select_online_courses(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('P34', 'online_courses')", 
     "Cursos online")


def _select_anonymized_degree_area(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('D3', 'anonymized_degree_area')", 
     "Área de formação")


def _select_anonymized_market_sector(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('D5', 'anonymized_manager_level')", 
     "Setor de mercado")


def _select_anonymized_role(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('D6', 'anonymized_role')", 
     "Cargo")


def _select_is_manager(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('P13', 'manager')", 
     "Cargo Gerencial")
    
def _select_anonymized_manager_role(df: pd.DataFrame) -> pd.DataFrame:
    return _default_selectbox(df,
     "('D5', 'anonymized_manager_level')", 
     "Nível Gerencial")


def _default_selectbox(
    df: pd.DataFrame, 
    column_name: str, 
    question: str) -> pd.DataFrame:
    options_list = ["-"]
    options_list.extend(list(df[column_name].unique()))
    selected_option =  st.sidebar.selectbox(
        question,
        options=options_list,
        index=0)

    if selected_option != "-":
        df = df[df[column_name] == selected_option]
    
    return df
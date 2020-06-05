import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def plot_salary(df: pd.DataFrame) -> None:
    if df.shape[0] != 0: 
        st.title("Geral")
        sns.kdeplot(df["('P16', 'salary_range')"], shade=True, legend=False)
        sns.despine()
        st.pyplot()
    else:
        st.markdown("> Nenhum participante respondeu com esses filtros")



def print_salary(df: pd.DataFrame) -> None:
    if df.shape[0] != 0:
        st.markdown("**Número de pessoas que responderam com esses filtros**: {}".format(df.shape[0]))
        st.markdown("**Mediana**: {}".format(int(df["('P16', 'salary_range')"].median())))
        st.markdown("**Máximo**: {}".format(df["('P16', 'salary_range')"].max()))
        st.markdown("**Mínimo**: {}".format(df["('P16', 'salary_range')"].min()))   


def plot_segmented_salary(df: pd.DataFrame, segmentation_column: str, title: str) -> None:
    if df.shape[0] != 0:
        try:
            unique_values = list(df[segmentation_column].unique())
            st.markdown("-----")
            st.title(f"Salários por {title}")
            unique_labels = []
            for value in unique_values:
                if df[df[segmentation_column] == value].shape[0] != 0:
                    g = sns.kdeplot(df[df[segmentation_column] == value]["('P16', 'salary_range')"], shade=True, legend=False)
                    unique_labels.append(value)
            sns.despine()
            plt.legend(labels=unique_labels)
            plt.show(g)
            st.pyplot()
        except Exception as e:
            st.markdown(f"> {e}")
    else:
        st.markdown("> Nenhum participante respondeu com esses filtros")
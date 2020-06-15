import pandas as pd
import streamlit as st
import altair as alt


def plot_salary(df: pd.DataFrame) -> None:
    if df.shape[0] != 0: 
        st.title("Geral")
        c = alt.Chart(df).transform_fold(
            ["salary_range"],
            as_=['Legenda', 'Salários']
        ).mark_area(
            opacity=0.7,
            interpolate='step'
        ).encode(
            alt.X('Salários:Q', bin=alt.Bin(maxbins=100)),
            alt.Y('count()', stack=None, axis=alt.Axis(title="Número de pessoas")),
        )
        st.altair_chart(c, use_container_width=True)
    else:
        st.markdown("> Nenhum participante respondeu com esses filtros")



def print_salary(df: pd.DataFrame) -> None:
    if df.shape[0] != 0:
        st.markdown("**Número de pessoas que responderam com esses filtros**: {}".format(df.shape[0]))
        st.markdown("**Mediana**: {}".format(int(df["salary_range"].median())))
        st.markdown("**Máximo**: {}".format(df["salary_range"].max()))
        st.markdown("**Mínimo**: {}".format(df["salary_range"].min()))   


def plot_segmented_salary(df: pd.DataFrame, segmentation_column: str, title: str) -> None:
    if df.shape[0] != 0:
        try:
            st.markdown("-----")
            st.title(f"Salários por {title}")
            df = df[~df[segmentation_column].isna()].copy()
            c = alt.Chart(df).transform_density(
                "salary_range",
                groupby=[segmentation_column],
                as_=['salary_range', 'density'],
            ).mark_area(
                opacity=0.5,
                interpolate='step'
            ).encode(
                alt.X('salary_range:Q', bin=alt.Bin(maxbins=100)),
                alt.Y('density:Q', stack=None),
                alt.Color(f'{segmentation_column}:N')
            )
            st.altair_chart(c, use_container_width=True)
        except Exception as e:
            st.markdown(f"> {e}")
    else:
        st.markdown("> Nenhum participante respondeu com esses filtros")
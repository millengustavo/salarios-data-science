import streamlit as st


def print_description() -> None:
    st.title("Salários em carreiras de dados")
    st.markdown("""
    > *Qual o salário dos profissionais de Data Science no Brasil? Descubra com esse aplicativo interativo!*

    Fonte dos dados: Pesquisa de mercado de Data Science feita pelo Data Hackers
    [https://www.kaggle.com/datahackers/pesquisa-data-hackers-2019](https://www.kaggle.com/datahackers/pesquisa-data-hackers-2019)
    """)
    st.sidebar.title("Filtros")
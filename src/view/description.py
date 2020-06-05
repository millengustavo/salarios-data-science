import streamlit as st


def print_description() -> None:
    st.title("Salários em carreiras de dados")
    st.markdown("""
    *Quanto estão ganhando as pessoas com características parecidas com a sua?*
    
    Fonte dos dados: Pesquisa de mercado de Data Science feita pelo Data Hackers
    [https://www.kaggle.com/datahackers/pesquisa-data-hackers-2019](https://www.kaggle.com/datahackers/pesquisa-data-hackers-2019)
    """)
    st.sidebar.title("Filtros")
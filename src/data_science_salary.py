import streamlit as st

from model.file import load_data

from view.description import print_description
from view.salary import plot_salary, print_salary, plot_segmented_salary

from controller.menu import filter_data


df = load_data()

print_description()

df = filter_data(df)

plot_salary(df)
print_salary(df)

plot_segmented_salary(df, "('P2', 'gender')", "gênero")
plot_segmented_salary(df, "('P1', 'age')", "idade")
plot_segmented_salary(df, "('P5', 'living_state')", "estado de residência")
plot_segmented_salary(df, "('P13', 'manager')", "tem cargo gerencial?")
plot_segmented_salary(df, "('P19', 'is_data_science_professional')", "é Data Scientist?")
plot_segmented_salary(df, "('P34', 'online_courses')", "fez cursos online?")

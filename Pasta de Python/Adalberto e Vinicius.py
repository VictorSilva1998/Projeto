import streamlit as st

nome = st.text_input("Qual é o seu nome?")

if st.button("Enviar"):
    if nome.strip() != "":
        st.success(f"Bom dia, {nome}! Tenha um excelente dia!")
    else:
        st.warning("Por favor, digite o seu nome antes de clicar.")
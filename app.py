import streamlit as st

st.title("Base Ativar/Inativar Itens")
st.text_input("SEQPRODUTO")
st.selectbox("Opções",["TODAS LOJAS (ATACADO/VAREJO)","SOMENTE ATACADO","SOMENTE VAREJO","LOJAS ESPECÍFICAS"])

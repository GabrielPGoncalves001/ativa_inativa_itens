import streamlit as st

st.title("Base Ativar/Inativar Itens")
st.text_input("SEQPRODUTO")
opcao = st.selectbox("Opções",
             ["TODAS LOJAS (ATACADO/VAREJO)",
              "SOMENTE ATACADO","SOMENTE VAREJO",
              "LOJAS ESPECÍFICAS"])
if opcao == "LOJAS ESPECÍFICAS":
  lojas = st.selectbox("Escolha a Filial",
                       ["1","3","5","7","9","11","12","13","14","15","16","19","25","26",
                        "27","28","29","30","31","32","33","34","35","41","43","44","45",
                        "47","48","50","51","53","54","55","56","57","58","201","202","203",
                        "204"]

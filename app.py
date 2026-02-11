import streamlit as st
import pandas as pd


st.title("Base Ativar/Inativar Itens")

with st.form("Base"):
  
  seqproduto = st.text_input("SEQPRODUTO")
  
  seleciona_lojas = st.selectbox("Opções",
               ["TODAS LOJAS (ATACADO/VAREJO)",
                "SOMENTE ATACADO","SOMENTE VAREJO",
                "LOJAS ESPECÍFICAS"])
  
  opcao = st.selectbox("Selecione a opção", ["ATIVAR","INATIVAR"])
  
  lojas = None
  
  if seleciona_lojas == "LOJAS ESPECÍFICAS":
    lojas = st.selectbox("Escolha a Filial",
                         ["1","3","5","7","9","11","12","13","14","15","16","19","25","26",
                          "27","28","29","30","31","32","33","34","35","41","43","44","45",
                          "47","48","50","51","53","54","55","56","57","58","201","202","203",
                          "204"])
  enviar = st.form_submit_button("Criar Base CSV")

if enviar:
  lojas_final = lojas if lojas else seleciona_lojas
  
  dados = {
    "SEQPRODUTO":[seqproduto],
    "LOJAS":[lojas_final],
    "STATUSVENDA":[opcao]
  }

  csv = pd.DataFrame(dados)

  csv_bytes = csv.to_csv(index=False, sep=';').encode("utf=8")
  st.download_button(
    label="Clique aqui para baixar o csv",
    data=csv_bytes,
    file_name="base_ativa_inativa.csv",
    mime="text/csv"
  )
                                             
                                             
  
  
  
  

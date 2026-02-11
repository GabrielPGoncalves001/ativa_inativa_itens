import streamlit as st
import pandas as pd
from datetime import datetime

agora = datetime.now().strftime('%d/%m/%Y %H:%M')
st.title("Base Ativar/Inativar Itens")

  
seqproduto = st.text_input("SEQPRODUTO")

seleciona_lojas = st.selectbox("Opções",
             ["TODAS LOJAS (ATACADO/VAREJO)",
              "SOMENTE ATACADO","SOMENTE VAREJO",
              "LOJAS ESPECÍFICAS"])



lojas = None

if seleciona_lojas == "LOJAS ESPECÍFICAS":
  lojas = st.selectbox("Escolha a Filial",
                       ["1","3","5","7","9","11","12","13","14","15","16","19","25","26",
                        "27","28","29","30","31","32","33","34","35","41","43","44","45",
                        "47","48","50","51","53","54","55","56","57","58","201","202","203",
                        "204"])

opcao = st.selectbox("Selecione a opção", ["ATIVAR","INATIVAR"])


if st.button("SALVAR"):
  
  st.write(f'Base Salva em: {agora}')  
  seq_list = [s.strip() for s in seqproduto.split(",") if s.strip() != ""]
  
  lojas_final = lojas if lojas else seleciona_lojas
  
  dados = {
    "SEQPRODUTO":seq_list,
    "LOJAS":[lojas_final]*len(seq_list),
    "STATUSCOMPRA":"A",
    "STATUSVENDA":[opcao]*len(seq_list)
  }

  csv = pd.DataFrame(dados)

  csv_bytes = csv.to_csv(index=False, sep=';').encode("utf=8")
  st.download_button(
    label="Clique aqui para baixar o csv",
    data=csv_bytes,
    file_name="base_ativa_inativa.csv",
    mime="text/csv"
  )
                                             
                                             
  
  
  
  

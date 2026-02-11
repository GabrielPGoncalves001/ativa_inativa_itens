import streamlit as st
import pandas as pd
from datetime import datetime

agora = datetime.now().strftime('%d/%m/%Y %H:%M')
st.title("Base Ativar/Inativar Itens")

df_base_import = pd.DataFrame(columns=['SEQPRODUTO'])
csv_import = df_base_import.to_csv(sep=';',
                                   index=False,
                                   encoding='utf-8').encode()
st.button("Clique aqui para entender como usar a interface"r)

st.download_button(
  label="Clique aqui para baixar a base para importar os códigos",
  data=csv_import,
  file_name="Base Import Ativa-Inativa.csv",
  mime="text/csv"
)

arquivo = st.file_uploader("Importe a base com os seqprodutos", type="csv")
seqproduto_list = []
if arquivo:
  df_upload = pd.read_csv(arquivo,
                          index_col=False,
                          encoding="utf-8",
                          sep=';')
  st.success('Arquivo importado com sucesso')

  if 'SEQPRODUTO' not in df_upload.columns:
    st.error('A base precisa conter a coluna de seqproduto')
  else:
    seqproduto_list = df_upload['SEQPRODUTO'].tolist()
    st.write("Foram encontrados", len(seqproduto_list), "códigos.")

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
  #seq_list = [s.strip() for s in seqproduto_list.split(",") if s.strip() != ""]
  
  lojas_final = lojas if lojas else seleciona_lojas
  
  df_dados = pd.DataFrame({
    "SEQPRODUTO":seqproduto_list,
    "LOJAS":[lojas_final]*len(seqproduto_list),
    "STATUSCOMPRA":[opcao]*len(seqproduto_list),
    "STATUSVENDA":"A"
  })
  
  csv_bytes = df_dados.to_csv(sep=';',encoding='utf-8',index=False).encode()
  st.download_button(
    label="Clique aqui para baixar o csv",
    data=csv_bytes,
    file_name="base_ativa_inativa.csv",
    mime="text/csv"
  )

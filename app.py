import streamlit as st
import requests
from random import randint
from PIL import Image

dados = requests.get("https://api.potterdb.com/v1/characters")
dados_dic = dados.json()

# Variável global para armazenar personagem atual
personagem_atual = ""

# Função para obter uma frase motivacional
def obter_frase():
  url = "https://api.potterdb.com/v1/characters"
  page_number = randint(1,46)
  resposta = requests.get(url + '?page[number]=' + str(page_number))
  
  if resposta.status_code == 200:
    dados = resposta.json()['data']
    random = randint(0,98)
    dadosLista = dados[random]
    personagem = dadosLista['attributes']['name']
    imagem = dadosLista['attributes']['image']
    wiki = dadosLista['attributes']['wiki']
    house = dadosLista['attributes']['house']
    
    if imagem:
      resposta = (f"Nome: {personagem} - Foto: {imagem} - House: {house}")
    else:
      resposta = (f"Nome: {personagem} - Link Wiki: {wiki} - House: {house}")
    return resposta

  else:
    print("Erro ao buscar personagem")
    return None


# Configurações gerais do Streamlit

st.set_page_config(
  page_title = "Harry Potter Characters",
  page_icon = "⚡",
  layout = "wide", # largura total da página
)

# importando e lendo o arquivo style.css
with open("style.css") as f:
  st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

# Botão
if st.button('Obter novo personagem'):
  frase_traduzida = obter_frase()
  personagem_atual = frase_traduzida # armazena a frase atual

# Titulo do site centralizado
st.markdown("<h1 style = 'text_align:center;'>⚡Harry Potter Characters⚡</h1>", unsafe_allow_html=True)

# Frase
st.subheader("Character:")
if personagem_atual:
  st.write(personagem_atual)

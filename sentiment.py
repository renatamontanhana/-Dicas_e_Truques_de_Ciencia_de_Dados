# -*- coding: utf-8 -*-
"""sentiment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dzy3IgoEi933meP5-rGG0QR-vTwYFhEk
"""

###################################
# Sistema de Satisfação do Cliente#
###################################


# Pacote de Implementação da Máquina Preditiva
import streamlit as st
# Pacote de PLN - NLTK - Natural Language Tool Kit
import nltk

# Titulo do sistema
st.write("# Análise de Satisfação do Cliente")

# Entrada de dados - A manifestação do Cliente
user_input = st.text_input("Por favor, avalie o nosso atendimento   :  ")

# Criação da Máquina Preditiva de Satisfação do Cliente
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

# Refinamento

if score == 0:
    st.write(" ")

elif score["neg"] != 0:
  st.write("### Análise Negativa")

elif score["pos"] != 0:
  st.write("### Análise Positiva")
import PyPDF2
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

def extract_text_from_pdf(file):
    """Extrai texto de um arquivo PDF, com melhor tratamento de erros."""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        st.error(f"Erro ao ler o arquivo PDF: {e}")
        return None

def get_api_key():
    """
    Obtém a chave da API do Google. Permite que o usuário insira a chave na interface,
    mas pré-carrega a chave do arquivo .env se ela existir.
    """
    st.sidebar.header("✨ Configuração")
   
    env_api_key = os.getenv("GOOGLE_API_KEY")
  
    api_key = st.sidebar.text_input(
        "Insira sua Chave da API do Google",
        type="password",
        value=env_api_key or "",  
        help="Você pode obter sua chave no Google AI Studio."
    )
    
    if env_api_key and api_key == env_api_key:
        st.sidebar.success("Chave da API carregada do .env!", icon="✅")
        
    return api_key

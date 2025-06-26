import streamlit as st
from utils import extract_text_from_pdf

def setup_ui():

    st.set_page_config(page_title="Gerador de Currículo com IA", layout="wide")
    st.title("🚀 Gerador de Currículo com IA")
    st.markdown("Otimize seu currículo para qualquer vaga, de forma inteligente.")

    user_data = ""
    
    st.header("1. Insira seus dados")
    input_method = st.radio("Escolha como fornecer seus dados:", ('Copiar e Colar Texto', 'Enviar PDF do LinkedIn'))

    if input_method == 'Copiar e Colar Texto':
        user_data = st.text_area("Cole aqui seu currículo atual ou informações profissionais:", height=300)
    else:
        uploaded_file = st.file_uploader("Faça o upload do seu currículo em PDF:", type=['pdf'])
        if uploaded_file is not None:
            with st.spinner('Extraindo texto do PDF...'):
                user_data = extract_text_from_pdf(uploaded_file)
            st.success('Texto extraído com sucesso!')
            st.text_area("Texto extraído do PDF:", value=user_data, height=300, disabled=True)

    st.header("2. Cole a descrição da vaga")
    job_description = st.text_area("Cole aqui os requisitos e a descrição da vaga desejada:", height=200)

    generate_button = st.button("✨ Gerar Currículo Otimizado", type="primary")

    return user_data, job_description, generate_button

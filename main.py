import streamlit as st
from ui import setup_ui
from generator import generate_resume
from document_creator import create_resume_docx, create_resume_pdf
from utils import get_api_key

def main():
    st.set_page_config(
        page_title="Gerador de Currículos Otimizados",
        page_icon=":briefcase:",
        layout="wide"
    )

    api_key = get_api_key()
    user_data, job_description, generate_button = setup_ui()

    if generate_button:
        if not api_key:
            st.error("Por favor, insira sua chave da API do Google na barra lateral para continuar.")
            return

        if not user_data or not job_description:
            st.error("Por favor, preencha todos os campos antes de gerar o currículo.")
            return

        with st.spinner("Aguarde, a mágica está acontecendo... ✨"):
            try:
                generated_resume = generate_resume(user_data, job_description, api_key)
                
                st.header("3. Seu Currículo Otimizado")
                st.markdown(generated_resume)

                resume_docx = create_resume_docx(generated_resume)
                
                resume_docx = create_resume_docx(generated_resume)
                resume_pdf = create_resume_pdf(generated_resume)

                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="📥 Baixar como Word (.docx)",
                        data=resume_docx,
                        file_name="curriculo_otimizado.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )
                with col2:
                    st.download_button(
                        label="📄 Baixar como PDF",
                        data=resume_pdf,
                        file_name="curriculo_otimizado.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

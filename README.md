# Gerador de Currículos com IA

Este projeto é uma aplicação web construída com Streamlit que utiliza a API do Google Gemini para otimizar currículos para vagas de emprego específicas. A ferramenta analisa o currículo do usuário e a descrição de uma vaga para gerar uma versão aprimorada e personalizada, destacando as experiências e habilidades mais relevantes.

## ✨ Funcionalidades

-   **Otimização com IA:** Utiliza o modelo de linguagem do Google Gemini para reescrever e adaptar seu currículo.
-   **Análise de Vagas:** Extrai palavras-chave e competências da descrição da vaga para alinhar seu currículo.
-   **Foco em Conquistas:** Transforma responsabilidades em conquistas mensuráveis e de impacto.
-   **Interface Amigável:** Interface simples e intuitiva construída com Streamlit.
-   **Upload de Currículo:** Suporta o envio de currículos em formato de texto ou PDF.
-   **Exportação Fácil:** Permite o download do currículo otimizado em formatos `.docx` e `.pdf`.
-   **Configuração Flexível de API:** Permite inserir a chave da API do Google diretamente na interface ou carregá-la de um arquivo `.env`.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python
-   **Interface Web:** Streamlit
-   **IA Generativa:** Google Gemini API
-   **Manipulação de Documentos:** `python-docx`, `fpdf2`
-   **Manipulação de PDF:** `PyPDF2`

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

-   Python 3.8 ou superior
-   Uma chave de API do Google Gemini. Você pode obter uma no [Google AI Studio](https://aistudio.google.com/app/apikey).

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/gerador-curriculo.git
    cd gerador-curriculo
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a chave da API:**
    Existem duas maneiras de configurar sua chave da API do Google:

    *   **Opção 1 (Recomendado): Arquivo `.env`**
        Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave:
        ```
        GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
        ```
        A aplicação carregará a chave automaticamente.

    *   **Opção 2: Pela Interface**
        Execute a aplicação e cole sua chave da API no campo "Insira sua Chave da API do Google" na barra lateral.

5.  **Execute a aplicação:**
    ```bash
    streamlit run main.py
    ```

A aplicação estará disponível em seu navegador no endereço `http://localhost:8501`.

## 📄 Como Usar

1.  Abra a aplicação no seu navegador.
2.  Insira sua chave da API na barra lateral (se não estiver usando o arquivo `.env`).
3.  Cole as informações do seu currículo atual ou faça o upload de um arquivo PDF.
4.  Cole a descrição completa da vaga para a qual você está se candidatando.
5.  Clique no botão "Gerar Currículo Otimizado".
6.  Aguarde a IA processar as informações.
7.  Visualize o resultado e faça o download em formato Word (.docx) ou PDF.

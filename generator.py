import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generate_resume(user_data, job_description, api_key):
    """Gera um currículo personalizado usando a API do Gemini."""
    if not api_key:
        raise ValueError("A chave da API do Google não foi fornecida. Insira-a na barra lateral.")

    genai.configure(api_key=api_key)
    # Recomenda-se usar um modelo mais robusto como o 1.5 Pro para tarefas complexas de análise e reescrita.
    # Se o 'gemini-2.0-flash' não entregar o resultado esperado, considere usar 'gemini-1.5-pro-latest'.
    model = genai.GenerativeModel('gemini-2.5-flash') 

    # --- PROMPT MELHORADO E OTIMIZADO ---
    prompt = f"""
    **Persona:** Você é um Especialista em RH e Coach de Carreira, perito em criar currículos de alto impacto que são aprovados tanto por sistemas de rastreamento de candidatos (ATS) quanto por recrutadores humanos. Sua especialidade é "traduzir" a experiência de um candidato para a linguagem exata de uma vaga.

    **Contexto:**
    - **Meus Dados:** (currículo atual, informações do LinkedIn ou texto livre do usuário)
    {user_data}

    - **Descrição da Vaga Alvo:**
    {job_description}

    **Tarefa Detalhada:**
    1.  **Análise Estratégica de Palavras-Chave (Otimização para ATS):**
        * Examine minuciosamente a "Descrição da Vaga" para identificar as principais competências, tecnologias, metodologias e qualificações exigidas (as "palavras-chave").
        * Crie uma lista interna dessas palavras-chave para guiar a criação do currículo.

    2.  **Criação de um Resumo Profissional de Alto Impacto:**
        * Elabore um resumo de 3 a 5 linhas que funcione como um "gancho". Ele deve espelhar diretamente os requisitos mais importantes da vaga, apresentando o candidato como a solução ideal.

    3.  **Reescrita da Experiência Profissional com Foco em Conquistas:**
        * Para cada cargo listado em "Meus Dados", reescreva as descrições. Transforme as responsabilidades do dia a dia em conquistas quantificáveis e impactantes.
        * Use verbos de ação fortes no início de cada tópico (ex: Otimizei, Desenvolvi, Liderei, Reduzi, Aumentei).
        * Incorpore as palavras-chave identificadas no passo 1 de forma natural e relevante dentro da descrição das experiências. O objetivo é mostrar *onde* e *como* o candidato aplicou as competências que a vaga exige.
        * Ajuste a ordem dos tópicos em cada experiência para destacar primeiro o que é mais relevante para a vaga alvo.

    4.  **Seleção e Organização de Habilidades:**
        * Crie uma seção de habilidades que seja um reflexo direto das exigências da vaga e das competências do usuário.
        * Mapeie as palavras-chave para as experiências reais do usuário, sem inventar competências. Se o usuário tem "experiência com X" e a vaga pede "domínio de X", use o termo da vaga.

    5.  **Formatação Limpa e Amigável para ATS:**
        * Use o template de saída fornecido. A formatação deve ser extremamente limpa, sem tabelas, colunas ou elementos gráficos. Isso garante que qualquer sistema ATS consiga ler as informações corretamente.
        * Não inclua informações pessoais de contato (endereço, telefone, email), conforme solicitado.
    
    6. **Não adicione textos extras sem ser parte do currículo:**
        

    **Princípio Fundamental:** O currículo final deve ser uma resposta direta e personalizada à vaga, mantendo-se fiel à experiência real do candidato. O objetivo não é mentir, mas sim enquadrar a verdade de forma estratégica.

    **Formato de Saída (Use este template rigorosamente):**

    **[Seu Nome]**

    **Resumo Profissional**
    [Texto do resumo de alto impacto aqui]

    **Experiência Profissional**

    **[Cargo mais recente]** | [Empresa] | [Período]
    * [Conquista 1, alinhada com a vaga e usando palavras-chave]
    * [Conquista 2, alinhada com a vaga e usando palavras-chave]
    * [Conquista 3, alinhada com a vaga e usando palavras-chave]

    **[Cargo anterior]** | [Empresa] | [Período]
    * [Conquista 1, alinhada com a vaga e usando palavras-chave]
    * [Conquista 2, alinhada com a vaga e usando palavras-chave]

    **Formação Acadêmica**
    [Seu curso] | [Instituição de Ensino] | [Ano de Conclusão]

    **Habilidades**
    * **Técnicas:** [Liste aqui as habilidades técnicas mais relevantes para a vaga, usando os termos exatos da descrição]
    * **Interpessoais:** [Liste aqui as soft skills relevantes para a vaga, como "Comunicação", "Liderança", "Resolução de Problemas"]
    * **Ferramentas/Tecnologias:** [Liste aqui softwares, plataformas e ferramentas específicas, como "Microsoft Office Suite", "JIRA", "SAP", "Python"]
    """

    response = model.generate_content(prompt)
    return response.text
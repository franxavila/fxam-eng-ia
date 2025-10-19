import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave do ambiente, não do código!
minha_chave_segura = os.getenv("GOOGLE_API_KEY")

# Agora use 'minha_chave_segura' no seu código

# 1. Inicializa o LLM (Gemini)
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# 2. Cria o Template do Prompt (O que queremos perguntar)
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de IA focado em negócios."),
    ("user", "{input}")
])

# 3. Cria um Parser (para extrair a resposta de texto)
output_parser = StrOutputParser()

# 4. Cria a "Chain" (Corrente)
#    Isto "prende" o prompt, o modelo e o parser juntos.
chain = prompt | llm | output_parser

# 5. Executa a Chain
print("--- Teste do Assistente de IA ---")
pergunta = "Qual a melhor forma de usar IA para otimizar um funil de vendas?"
resposta = chain.invoke({"input": pergunta})

print(f"Pergunta: {pergunta}")
print(f"Resposta: {resposta}")
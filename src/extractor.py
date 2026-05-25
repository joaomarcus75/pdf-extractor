import os
from groq import Groq
from dotenv import load_dotenv

# Lê o arquivo .env e joga as variáveis pro ambiente
load_dotenv()

# Cria o cliente da Groq usando a key do .env
client = Groq(api_key=os.environ["GROQ_API_KEY"])


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    resposta = call_llm("Explain in 2 sentences what a token is in LLMs.")
    print(resposta)
from time import time
from groq import Groq
client = Groq(
   api_key="Chave_api"
)
tempo_inicial = time()

response = client.chat.completions.create(
   model="openai/gpt-oss-120b",
   messages=[
       {
           "role": "system",
           "content": "Você é um assistente útil e objetivo."
       },
       {
           "role": "user",
           "content": "Explique o que é inteligência artificial."
       }
   ]
)

tempo_final = time()
print(f"Tempo da requisição: {tempo_final - tempo_inicial}s")
print(response.choices[0].message.content)


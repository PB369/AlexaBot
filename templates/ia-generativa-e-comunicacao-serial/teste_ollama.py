import requests
while True:
    texto = input("Você: ")
    prompt = "Responda de forma breve com no máximo 50 palavras isto:"+ texto
    if texto.lower() in ["sair", "exit", "quit"]:
        break
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "ministral-3:8b",
            "prompt": texto,
            "stream": False
        })
    resposta = response.json()
    print("Llama:", resposta['response'])
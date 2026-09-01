import requests

class Ollama:
    def __init__(
        self,
        url="http://localhost:11434/api/generate",
        model="ministral-3:latest"
    ):
        self.url = url
        self.model = model

    def ask(self, texto):
        prompt = (
            "Responda de forma breve, "
            "sem markdown e sem emojis: "
            + texto
        )
        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )

            response.raise_for_status()
            resposta = response.json()
            return resposta["response"]
        
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Não foi possível conectar ao Ollama.")

        except requests.exceptions.RequestException as erro:
            raise RuntimeError(f"Erro na requisição ao Ollama: {erro}")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")
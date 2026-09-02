import requests


class WeatherService:

    def __init__(self):
        self.geocoding_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
        )

        self.forecast_url = (
            "https://api.open-meteo.com/v1/forecast"
        )

    def buscar_cidade(self, cidade):

        parametros = {
            "name": cidade,
            "count": 1,
            "language": "pt",
            "format": "json"
        }

        resposta = requests.get(
            self.geocoding_url,
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        if "results" not in dados or not dados["results"]:
            return None

        resultado = dados["results"][0]

        return {
            "nome": resultado["name"],
            "latitude": resultado["latitude"],
            "longitude": resultado["longitude"],
            "pais": resultado.get("country", "")
        }

    def obter_previsao(self, cidade):

        local = self.buscar_cidade(cidade)

        if local is None:
            return None

        parametros = {
            "latitude": local["latitude"],
            "longitude": local["longitude"],
            "current": (
                "temperature_2m,"
                "apparent_temperature,"
                "precipitation,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "daily": (
                "weather_code,"
                "temperature_2m_max,"
                "temperature_2m_min,"
                "precipitation_probability_max"
            ),
            "forecast_days": 1,
            "timezone": "auto"
        }

        resposta = requests.get(
            self.forecast_url,
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        return {
            "cidade": local["nome"],
            "temperatura": dados["current"]["temperature_2m"],
            "sensacao": dados["current"]["apparent_temperature"],
            "codigo_tempo": dados["current"]["weather_code"],
            "chuva": dados["current"]["precipitation"],
            "vento": dados["current"]["wind_speed_10m"],
            "maxima": dados["daily"]["temperature_2m_max"][0],
            "minima": dados["daily"]["temperature_2m_min"][0],
            "probabilidade_chuva": (
                dados["daily"]["precipitation_probability_max"][0]
            )
        }

    def descricao_tempo(self, codigo):

        descricoes = {
            0: "céu limpo",
            1: "principalmente ensolarado",
            2: "parcialmente nublado",
            3: "nublado",
            45: "neblina",
            48: "neblina",
            51: "garoa leve",
            53: "garoa moderada",
            55: "garoa intensa",
            61: "chuva leve",
            63: "chuva moderada",
            65: "chuva forte",
            71: "neve leve",
            73: "neve moderada",
            75: "neve forte",
            80: "pancadas de chuva leves",
            81: "pancadas de chuva moderadas",
            82: "pancadas de chuva fortes",
            95: "trovoada",
            96: "trovoada com granizo",
            99: "trovoada forte com granizo"
        }

        return descricoes.get(
            codigo,
            "condições climáticas desconhecidas"
        )

    def gerar_resposta(self, cidade):

        previsao = self.obter_previsao(cidade)

        if previsao is None:
            return (
                f"Não encontrei informações sobre "
                f"o tempo em {cidade}."
            )

        descricao = self.descricao_tempo(
            previsao["codigo_tempo"]
        )

        return (
            f"A previsão para {previsao['cidade']} hoje "
            f"é de {descricao}. "
            f"A temperatura atual é de "
            f"{previsao['temperatura']:.0f} graus, "
            f"com sensação de "
            f"{previsao['sensacao']:.0f} graus. "
            f"A máxima será de "
            f"{previsao['maxima']:.0f} graus "
            f"e a mínima de "
            f"{previsao['minima']:.0f} graus. "
            f"A probabilidade de chuva é de "
            f"{previsao['probabilidade_chuva']} por cento."
        )
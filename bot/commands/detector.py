import re

class CommandDetector:
    WAKE_WORDS = [ "alexa", "alexia", "alex" ] 

    EXIT_COMMANDS = [ "sair", "tchau", "encerrar conversa", "sair da conversa" ]

    AGENDA_ADD_COMMANDS = [ "cadastrar evento na agenda", "cadastrar evento", "adicionar evento na agenda", "adicionar evento" ]
    AGENDA_READ_COMMANDS = [ "ler agenda", "mostrar agenda", "listar agenda", "consultar agenda"]
    AGENDA_CLEAR_COMMANDS = ["limpar agenda", "limpar a agenda", "apagar agenda", "apagar a agenda"]

    FACE_COMMANDS = ["reconhecer face", "reconhecer minha face", "reconhecer meu rosto", "quem sou eu", "identificar pessoa", "identificar meu rosto"]

    YOUTUBE_COMMANDS = ["abrir youtube", "abra o youtube", "abrir o youtube", "abre o youtube", "abra youtube", "abre youtube"]

    WEATHER_COMMANDS = ["previsão do tempo", "previsao do tempo", "previsão do clima", "previsao do clima", "tempo para", "clima para"]
    
    def normalize(self, texto):
        texto = texto.lower()
        # Remove pontuação de fala, mas preserva operadores matemáticos.
        texto = re.sub(r"[!?;:]", "", texto)
        texto = re.sub(r"\s+", " ", texto)
        return texto.strip()

    def has_wake_word(self, texto):
        texto = self.normalize(texto)
        palavras = texto.split()
        return any(palavra in palavras for palavra in self.WAKE_WORDS)

    def remove_wake_word(self, texto):
        texto = re.sub(
            r"\b(alexa|alexia|alex)\b",
            "",
            texto,
            flags=re.IGNORECASE
        )

        return re.sub(r"\s+", " ", texto).strip()

    def is_exit_command(self, texto):
        texto = self.normalize(texto)
        return texto in self.EXIT_COMMANDS

    def is_add_agenda_command(self, texto): 
        texto = self.normalize(texto) 
        return texto in self.AGENDA_ADD_COMMANDS 

    def is_read_agenda_command(self, texto): 
        texto = self.normalize(texto)
        return texto in self.AGENDA_READ_COMMANDS

    def is_clear_agenda_command(self, texto):
        texto = self.normalize(texto)
        return texto in self.AGENDA_CLEAR_COMMANDS

    def is_face_recognition_command(self, texto):
        texto = self.normalize(texto)
        return texto in self.FACE_COMMANDS

    def is_youtube_command(self, texto):
        texto = self.normalize(texto)

        return any(
            comando in texto
            for comando in self.YOUTUBE_COMMANDS
        )

    def extrair_tema_youtube(self, texto):
        texto = self.normalize(texto)

        padroes = [
            r"abra(?: o)? youtube e (?:rode|reproduza|coloque|pesquise) (?:um )?(?:vídeo|video) (?:sobre|de) (.+)",
            r"abrir(?: o)? youtube e (?:rodar|reproduzir|colocar|pesquisar) (?:um )?(?:vídeo|video) (?:sobre|de) (.+)",
            r"abra(?: o)? youtube (?:e )?(?:pesquise|procure) (?:por )?(?:um )?(?:vídeo|video)? (?:sobre|de)? ?(.+)",
            r"abrir(?: o)? youtube (?:e )?(?:pesquisar|procurar) (?:por )?(?:um )?(?:vídeo|video)? (?:sobre|de)? ?(.+)",
        ]

        for padrao in padroes:
            resultado = re.search(padrao, texto)

            if resultado:
                return resultado.group(1).strip()

        return None
    
    def is_weather_command(self, texto):
        texto = self.normalize(texto)

        return any(
            comando in texto
            for comando in self.WEATHER_COMMANDS
        )

    def extrair_cidade_weather(self, texto):

        texto = self.normalize(texto)

        padroes = [
            r"qual a previsão do tempo para (.+)",
            r"qual a previsao do tempo para (.+)",
            r"qual a previsão do clima para (.+)",
            r"qual a previsao do clima para (.+)",
            r"previsão do tempo para (.+)",
            r"previsao do tempo para (.+)",
            r"previsão do clima para (.+)",
            r"previsao do clima para (.+)",
            r"tempo para (.+)",
            r"clima para (.+)",
        ]

        for padrao in padroes:

            resultado = re.search(
                padrao,
                texto
            )

            if resultado:
                return resultado.group(1).strip()

        return None
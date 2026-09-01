import re

class CommandDetector:
    WAKE_WORDS = [ "alexa", "alexia", "alex" ] 

    EXIT_COMMANDS = [ "sair", "tchau", "encerrar conversa", "sair da conversa" ]

    AGENDA_ADD_COMMANDS = [ "cadastrar evento na agenda", "cadastrar evento", "adicionar evento na agenda", "adicionar evento" ]
    AGENDA_READ_COMMANDS = [ "ler agenda", "mostrar agenda", "consultar agenda"]
    AGENDA_CLEAR_COMMANDS = ["limpar agenda", "limpar a agenda", "apagar agenda", "apagar a agenda"]

    FACE_COMMANDS = ["reconhecer face", "reconhecer minha face", "reconhecer meu rosto", "quem sou eu", "identificar pessoa", "identificar meu rosto"]

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
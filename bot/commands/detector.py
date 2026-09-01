import re

class CommandDetector:
    WAKE_WORDS = [
        "alexa",
        "alexia",
        "alex"
    ]

    EXIT_COMMANDS = [
        "sair",
        "exit",
        "quit",
        "tchau",
        "ate mais",
        "encerrar conversa",
        "sair da conversa"
    ]

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
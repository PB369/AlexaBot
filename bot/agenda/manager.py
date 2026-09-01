from pathlib import Path

class AgendaManager:
    def __init__(self, arquivo="./data/agenda.txt"):
        self.arquivo = (Path(__file__).parent / "data" / "agenda.txt")

        # Cria a pasta caso ela não exista
        self.arquivo.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Cria o arquivo caso ele não exista
        self.arquivo.touch(exist_ok=True)

    def adicionar_evento(self, evento):
        evento = evento.strip()
        if not evento:
            return False

        with self.arquivo.open(
            "a",
            encoding="utf-8"
        ) as arquivo:
            arquivo.write(evento + "\n")
        return True

    def ler_eventos(self):
        with self.arquivo.open(
            "r",
            encoding="utf-8"
        ) as arquivo:
            eventos = [
                linha.strip()
                for linha in arquivo
                if linha.strip()
            ]

        return eventos

    def limpar_agenda(self):
        with self.arquivo.open("w", encoding="utf-8") as arquivo:
            arquivo.write("")

        return True
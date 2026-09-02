import cv2
from pathlib import Path


class Capturador:

    def __init__(self):

        # Pasta raiz do projeto
        raiz_projeto = Path(__file__).resolve().parent

        # Haar Cascade
        self.caminhoHaarCascade = (
            raiz_projeto
            / "bot"
            / "utils"
            / "haarcascade_frontalface_default.xml"
        )

        self.cascade = cv2.CascadeClassifier(
            str(self.caminhoHaarCascade)
        )

        if self.cascade.empty():
            raise Exception(
                f"Erro ao carregar o Haar Cascade:\n"
                f"{self.caminhoHaarCascade}"
            )

        # Webcam
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Não foi possível abrir a webcam.")

        # Tamanho das imagens
        self.largura = 220
        self.altura = 220

    def capturar(self, nome, pasta, quantidade=50):

        # Salva dentro de bot/
        raiz_projeto = Path(__file__).resolve().parent

        pasta_saida = (
            raiz_projeto
            / "bot"
            / pasta
        )

        pasta_saida.mkdir(
            parents=True,
            exist_ok=True
        )

        amostra = 1

        print()
        print("===================================")
        print("      CAPTURA DE FACES")
        print("===================================")
        print()
        print("Pressione T para tirar uma foto.")
        print("Pressione Q para sair.")
        print()

        while amostra <= quantidade:

            status, imagem = self.camera.read()

            if not status:
                print("Não foi possível capturar imagem.")
                break

            imagemCinza = cv2.cvtColor(
                imagem,
                cv2.COLOR_BGR2GRAY
            )

            faces = self.cascade.detectMultiScale(
                imagemCinza,
                scaleFactor=1.05,
                minSize=(150, 150)
            )

            # Desenha os rostos detectados
            for x, y, largura, altura in faces:

                cv2.rectangle(
                    imagem,
                    (x, y),
                    (x + largura, y + altura),
                    (0, 0, 255),
                    2
                )

            # Mostra instruções na tela
            cv2.putText(
                imagem,
                "T = Capturar | Q = Sair",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.putText(
                imagem,
                f"Fotos: {amostra - 1}/{quantidade}",
                (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.imshow(
                "Captura de rosto",
                imagem
            )

            tecla = cv2.waitKey(1) & 0xFF

            # Q = sair
            if tecla == ord("q"):
                print("Captura interrompida.")
                break

            # T = tirar foto
            if tecla == ord("t"):

                if len(faces) == 0:
                    print("Nenhum rosto detectado. Tente novamente.")
                    continue

                # Usa o primeiro rosto detectado
                x, y, largura, altura = faces[0]

                rosto = imagemCinza[
                    y:y + altura,
                    x:x + largura
                ]

                rosto = cv2.resize(
                    rosto,
                    (self.largura, self.altura)
                )

                caminho = (
                    pasta_saida
                    / f"{nome}_{amostra}.jpg"
                )

                cv2.imwrite(
                    str(caminho),
                    rosto
                )

                print(
                    f"Foto {amostra}/{quantidade} salva: "
                    f"{caminho}"
                )

                amostra += 1

        self.camera.release()
        cv2.destroyAllWindows()

        print()
        print("Captura finalizada.")
        print(f"Fotos salvas em: {pasta_saida}")


# ===================================
# EXECUÇÃO
# ===================================

capturador = Capturador()

nome = input(
    "Digite o nome da pessoa: "
)

pasta = input(
    "Digite a pasta onde deseja salvar "
    "(fotos ou desconhecidos): "
)

capturador.capturar(
    nome,
    pasta,
    quantidade=50
)
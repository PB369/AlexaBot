import cv2
from pathlib import Path

class FaceRecognizer:
    def __init__(self, modelo="models/classificadoreigen.yml"):
        self.modelo = Path(modelo)
        raiz_projeto = Path(__file__).resolve().parents[1]
        self.caminhoHaarCascade = (raiz_projeto / "utils" / "haarcascade_frontalface_default.xml")

        self.detector = cv2.CascadeClassifier(
            str(self.caminhoHaarCascade)
        )

        if self.detector.empty():
            raise Exception(
                f"Erro ao carregar o classificador Haar Cascade: "
                f"{self.caminhoHaarCascade}"
            )
        self.reconhecedor = cv2.face.EigenFaceRecognizer_create()
        self.reconhecedor.read(str(self.modelo))
        self.nomes = {
            1: "Pedro"
        }
        self.limiar_confianca = 8500

    def reconhecer(self):
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("Não foi possível abrir a webcam.")
            return None
        pessoa_reconhecida = None

        try:
            while True:
                status, imagem = camera.read()
                if not status:
                    print("Não foi possível capturar imagem.")
                    break
                imagem_cinza = cv2.cvtColor(imagem,  cv2.COLOR_BGR2GRAY)
                faces = self.detector.detectMultiScale(
                    imagem_cinza,
                    scaleFactor=1.5,
                    minSize=(30, 30)
                )

                for x, y, largura, altura in faces:
                    imagem_face = imagem_cinza[
                        y:y + altura,
                        x:x + largura
                    ]
                    imagem_face = cv2.resize(
                        imagem_face,
                        (220, 220)
                    )
                    id_pessoa, confianca = (self.reconhecedor.predict(imagem_face))
                    if confianca < self.limiar_confianca:
                        nome = self.nomes.get(id_pessoa,"Desconhecido")
                    else:
                        nome = "Desconhecido"

                    cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 255, 0), 2)
                    cv2.putText(imagem, f"{nome}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    print(f"Reconhecimento: {nome} (confianca: {confianca:.2f})")
                    pessoa_reconhecida = nome

                cv2.imshow("Reconhecimento facial", imagem)
                tecla = cv2.waitKey(1) & 0xFF
                if tecla == ord("q"):
                    break

        finally:
            camera.release()
            cv2.destroyAllWindows()

        return pessoa_reconhecida
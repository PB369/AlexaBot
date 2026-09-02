import cv2
import numpy as np
from pathlib import Path


# ==========================================
# CONFIGURAÇÃO
# ==========================================

raiz_projeto = Path(__file__).resolve().parent

pasta_pedro = raiz_projeto / "peopleFaces" / "pedro"
pasta_desconhecidos = raiz_projeto / "peopleFaces" / "desconhecidos"

pasta_modelos = raiz_projeto / "models"
pasta_modelos.mkdir(parents=True, exist_ok=True)

caminho_modelo = pasta_modelos / "classificadoreigen.yml"


# ==========================================
# CARREGAR IMAGENS
# ==========================================

faces = []
nomes = []


def carregar_faces(pasta, identificador):
    
    imagens = list(pasta.glob("*.jpg"))
    imagens += list(pasta.glob("*.jpeg"))
    imagens += list(pasta.glob("*.png"))

    print(f"\nPasta: {pasta}")
    print(f"Imagens encontradas: {len(imagens)}")

    for caminho_imagem in imagens:

        imagem = cv2.imread(str(caminho_imagem))

        if imagem is None:
            print(f"Não foi possível carregar: {caminho_imagem}")
            continue

        # Converte para escala de cinza
        imagem_cinza = cv2.cvtColor(
            imagem,
            cv2.COLOR_BGR2GRAY
        )

        # Garante o mesmo tamanho usado no reconhecimento
        imagem_cinza = cv2.resize(
            imagem_cinza,
            (220, 220)
        )

        faces.append(imagem_cinza)
        nomes.append(identificador)

        print(
            f"Carregada: {caminho_imagem.name} "
            f"-> ID {identificador}"
        )


# ==========================================
# PEDRO = ID 1
# ==========================================

carregar_faces(
    pasta_pedro,
    1
)


# ==========================================
# DESCONHECIDOS = ID 0
# ==========================================

carregar_faces(
    pasta_desconhecidos,
    0
)


# ==========================================
# VERIFICAÇÃO
# ==========================================

if len(faces) == 0:
    raise Exception(
        "Nenhuma imagem foi encontrada para treinamento."
    )

if len(set(nomes)) < 2:
    raise Exception(
        "É necessário ter imagens de Pedro e de desconhecidos."
    )


print()
print("===================================")
print("RESUMO DO TREINAMENTO")
print("===================================")
print(f"Total de imagens: {len(faces)}")
print(f"Pedro (ID 1): {nomes.count(1)}")
print(f"Desconhecidos (ID 0): {nomes.count(0)}")


# ==========================================
# TREINAMENTO
# ==========================================

print()
print("Treinando modelo EigenFace...")

eigen = cv2.face.EigenFaceRecognizer_create()

eigen.train(
    faces,
    np.array(nomes)
)


# ==========================================
# SALVAR MODELO
# ==========================================

eigen.write(
    str(caminho_modelo)
)

print()
print("===================================")
print("TREINAMENTO CONCLUÍDO!")
print("===================================")
print(f"Modelo salvo em:")
print(caminho_modelo)
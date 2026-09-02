import cv2

for indice in range(5):

    camera = cv2.VideoCapture(indice)

    if camera.isOpened():
        print(f"✓ Câmera encontrada no índice {indice}")
        camera.release()
    else:
        print(f"✗ Nenhuma câmera no índice {indice}")
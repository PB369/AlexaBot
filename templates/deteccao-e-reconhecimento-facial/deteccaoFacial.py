import cv2

detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

imagem = cv2.imread('people.jpeg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = detector.detectMultiScale(imagem_cinza)
print(faces)

for x, y, l, a in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x + a, y + a), (0,0, 255), 2)

cv2.imshow('Imagem carregada', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
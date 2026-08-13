import cv2

camera = cv2.VideoCapture(0)
# lê um haar cascade para detectar faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while cv2.waitKey(1) == -1:
    status, frame = camera.read()
    print(status)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    print('Número de faces detectadas:', len(faces))

    # loop para desenhar os retângulos
    for (x,y,w,h) in faces:
       frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    cv2.imshow("Faces", frame)

camera.release()
cv2.destroyAllWindows()



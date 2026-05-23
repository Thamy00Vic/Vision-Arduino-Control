import cv2
import mediapipe as mp

mp_maos = mp.solutions.hands
maos = mp_maos.Hands()
mp_desenho = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()

    imagemRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = maos.process(imagemRGB)

    if resultado.multi_hand_landmarks:
        for mao in resultado.multi_hand_landmarks:
            mp_desenho.draw_landmarks(frame, mao, mp_maos.HAND_CONNECTIONS)

    cv2.imshow("Detector de Mao", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
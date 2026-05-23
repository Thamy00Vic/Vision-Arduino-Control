import cv2
import mediapipe as mp
import serial
import time

arduino = serial.Serial('COM3',9600)
time.sleep(2)

mp_maos = mp.solutions.hands
maos = mp_maos.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_desenho = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)
while True:
    sucesso, frame = camera.read()

    imagemRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = maos.process(imagemRGB)

    dedos = 0

    if resultado.multi_hand_landmarks:
        for mao in resultado.multi_hand_landmarks:

            mp_desenho.draw_landmarks(frame, mao, mp_maos.HAND_CONNECTIONS)

            pontos = mao.landmark

            if pontos[8].y < pontos[6].y:
                dedos += 1
            if pontos[12].y < pontos[10].y:
                dedos += 1
            if pontos[16].y < pontos[14].y:
                dedos += 1
            if pontos[20].y < pontos[18].y:
                dedos += 1

    if dedos >= 3:
        arduino.write(b'1')
        cv2.putText(frame,"LED LIGADO",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    else:
        arduino.write(b'0')
        cv2.putText(frame,"LED DESLIGADO",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("Controle por Mao",frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
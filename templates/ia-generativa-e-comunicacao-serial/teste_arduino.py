import serial
import time
arduino = serial.Serial("COM9", 9600, timeout=1)
time.sleep(2)
print("Digite 'on' para ligar ou 'off' para desligar.")
print("Digite 'sair' para encerrar.")
while True:
    comando = input("Comando: ").strip().lower()
    if comando == "on":
        arduino.write(b"a")
        print("Enviado: a")
    elif comando == "off":
        arduino.write(b"b")
        print("Enviado: b")
    elif comando == "sair":
        break
    else:
        print("Comando inválido. Use 'on' ou 'off'.")

arduino.close()
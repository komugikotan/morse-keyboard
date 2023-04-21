import serial
import time
import pyautogui

ser = serial.Serial('COM4', 9600) 
not_used = ser.readline()
status = 0
morse = "";

while True:
    val_decoded = ser.readline()

    if b'click' in val_decoded:
        status = 1
        tic = time.perf_counter()
        print("you pressed")
    else:
        if status == 1:
            toc = time.perf_counter()
            pressed_time = toc - tic
            print(f"You pressed button for {pressed_time} seconds")
            if pressed_time > 0.19:
                morse = morse + "_"
            if pressed_time < 0.2:
                morse = morse + "."
            

            print(morse)
ser.close()

#https://www.youtube.com/@LinusTechTips/playlists
#Sens4tion#0938

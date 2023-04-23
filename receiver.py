import serial
import time
import pyautogui

#change -'s speed your own
speed = 0.3
space_speed = 0.7

status = 2
morse = ""
morse_output = ""
blank = ""
blank_s = ""
tontu = ""
tontu_s = ""

while(True):
    ser = serial.Serial('COM6', 9600) 
    not_used = ser.readline()

    while True:
        val_decoded = ser.readline()

        if b'click' in val_decoded:     
            status = 1
            tontu = time.perf_counter()
            print("you pressed")

            print(morse_output)
            print(morse)
            
            try:
                blank_s = time.perf_counter()
                blank_time = blank_s - blank

                if blank_time > speed:
                    if (morse == ".-"):
                        morse_output = morse_output + "a"
                        pyautogui.write('a')
                        morse = ""
                    elif (morse == "-..."):
                        morse_output = morse_output + "b"
                        pyautogui.write('b')
                        morse = ""
                    elif (morse == "-.-."):
                        morse_output = morse_output + "c"
                        pyautogui.write('c')
                        morse = ""
                    elif (morse == "-.."):
                        morse_output = morse_output + "d"
                        pyautogui.write('d')
                        morse = ""
                    elif (morse == "."):
                        morse_output = morse_output + "e"
                        pyautogui.write('e')
                        morse = ""
                    elif (morse == "..-."):
                        morse_output = morse_output + "f"
                        pyautogui.write('f')
                        morse = ""
                    elif (morse == "--."):
                        morse_output = morse_output + "g"
                        pyautogui.write('g')
                        morse = ""
                    elif (morse == "...."):
                        morse_output = morse_output + "h"
                        pyautogui.write('h')
                        morse = ""
                    elif (morse == ".."):
                        morse_output = morse_output + "i"
                        pyautogui.write('i')
                        morse = ""
                    elif (morse == ".---"):
                        morse_output = morse_output + "j"
                        pyautogui.write('j')
                        morse = ""
                    elif (morse == "-.-"):
                        morse_output = morse_output + "k"
                        pyautogui.write('k')
                        morse = ""
                    elif (morse == ".-.."):
                        morse_output = morse_output + "l"
                        pyautogui.write('l')
                        morse = ""
                    elif (morse == "--"):
                        morse_output = morse_output + "m"
                        pyautogui.write('m')
                        morse = ""
                    elif (morse == "-."):
                        morse_output = morse_output + "n"
                        pyautogui.write('n')
                        morse = ""
                    elif (morse == "---"):
                        morse_output = morse_output + "o"
                        pyautogui.write('o')
                        morse = ""
                    elif (morse == ".--."):
                        morse_output = morse_output + "p"
                        pyautogui.write('p')
                        morse = ""
                    elif (morse == "--.-"):
                        morse_output = morse_output + "q"
                        pyautogui.write('q')
                        morse = ""
                    elif (morse == ".-."):
                        morse_output = morse_output + "r"
                        pyautogui.write('r')
                        morse = ""
                    elif (morse == "..."):
                        morse_output = morse_output + "s"
                        pyautogui.write('s')
                        morse = ""
                    elif (morse == "-"):
                        morse_output = morse_output + "t"
                        pyautogui.write('t')
                        morse = ""
                    elif (morse == "..-"):
                        morse_output = morse_output + "u"
                        pyautogui.write('u')
                        morse = ""
                    elif (morse == "...-"):
                        morse_output = morse_output + "v"
                        pyautogui.write('v')
                        morse = ""
                    elif (morse == ".--"):
                        morse_output = morse_output + "w"
                        pyautogui.write('w')
                        morse = ""
                    elif (morse == "-..-"):
                        morse_output = morse_output + "x"
                        pyautogui.write('x')
                        morse = ""
                    elif (morse == "-.--"):
                        morse_output = morse_output + "y"
                        pyautogui.write('y')
                        morse = ""
                    elif (morse == "--.."):
                        morse_output = morse_output + "z"
                        pyautogui.write('z')
                        morse = ""
                    elif (morse == ".----"):
                        morse_output = morse_output + "1"
                        pyautogui.write('1')
                        morse = ""
                    elif (morse == "..---"):
                        morse_output = morse_output + "2"
                        pyautogui.write('2')
                        morse = ""
                    elif (morse == "...--"):
                        morse_output = morse_output + "3"
                        pyautogui.write('3')
                        morse = ""
                    elif (morse == "....-"):
                        morse_output = morse_output + "4"
                        pyautogui.write('4')
                        morse = ""
                    elif (morse == "....."):
                        morse_output = morse_output + "5"
                        pyautogui.write('5')
                        morse = ""
                    elif (morse == "-...."):
                        morse_output = morse_output + "6"
                        pyautogui.write('6')
                        morse = ""
                    elif (morse == "--..."):
                        morse_output = morse_output + "7"
                        pyautogui.write('7')
                        morse = ""
                    elif (morse == "---.."):
                        morse_output = morse_output + "8"
                        pyautogui.write('8')
                        morse = ""
                    elif (morse == "----."):
                        morse_output = morse_output + "9"
                        pyautogui.write('9')
                        morse = ""
                    elif (morse == "-----"):
                        morse_output = morse_output + "0"
                        pyautogui.write('0')
                        morse = ""
                    else:
                        morse_output = morse_output + "*"
                        pyautogui.write('*')
                        morse = ""

                if blank_time > space_speed:
                    morse_output = morse_output + " "
                    pyautogui.write(' ')
                    morse = ""

            except:
                pass
    
        else:
            if status == 1:
                tontu_s = time.perf_counter()
                pressed_time = tontu_s - tontu
                if pressed_time > speed:
                    morse = morse + "-"
                if pressed_time < speed:
                    morse = morse + "."

                blank = time.perf_counter()
                
                status = 0


        
                


    ser.close()

    
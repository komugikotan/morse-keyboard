#import libraries
import serial
import time
import pyautogui
import pyperclip

#dash's speed
speed = 0.3
#spaces' speed
space_speed = 0.7

#Morse type (Japanese or Roman)
#If you want Roman morse, you set variable "type" to 1. If you want Japanese morse, you set variable "type" to 2.
type = 1

status = 2
morse = ""
morse_output = ""
blank = ""
blank_s = ""
tontu = ""
tontu_s = ""

#type Japanese by copy and pasting
def type_nihongo(letters):
    pyperclip.copy(letters)
    pyautogui.hotkey('ctrl', 'v')

#Dictionaly (morse_2_english)
english_morse_dict = {
    ".-":"a",
    "-...":"b", 
    "-.-.":"c",
    "-..":"d",
    ".":"e", 
    "..-.":"f",
    "--.":"g",
    "....":"h", 
    "..":"i",
    ".---":"j",
    "-.-":"k", 
    ".-..":"l",
    "--":"m",
    "-.":"n", 
    "---":"o",
    ".--.":"p",
    "--.-":"q", 
    ".-.":"r",
    "...":"s",
    "-":"t", 
    "..-":"u",
    "...-":"v",
    ".--":"w", 
    "-..-":"x",
    "-.--":"y",
    "--..":"z", 
    ".----":"1",
    "..---":"2",
    "...--":"3", 
    "....-":"4",
    ".....":"5",
    "-....":"6", 
    "--...":"7",
    "---..":"8",
    "----.":"9", 
    "-----":"0",
    ".-.-.-":".",
    "--..--":",",
    "---...":":", 
    "..--..":"?",
    "..--.-":"_",
    ".-.-.":"+", 
    "-....-":"-",
    "......":"^", 
    "-..-.":"/"
}

#dictionaly(morse_2_japanese)
japanese_morse_dict = {
    ".----":"1",
    "..---":"2",
    "...--":"3", 
    "....-":"4",
    ".....":"5",
    "-....":"6", 
    "--...":"7",
    "---..":"8",
    "----.":"9", 
    "-----":"0",
    ".-":"イ", 
    ".-.-":"ロ",
    "-...":"ハ",
    "-.-.":"ニ", 
    "-..":"ホ",
    ".":"ヘ",
    "..-..":"ト", 
    "..-.":"チ",
    "--.":"リ",
    "....":"ヌ", 
    "-.--.":"ル",
    ".---":"ヲ",
    "-.-":"ワ", 
    ".-..":"カ",
    "--":"ヨ",
    "-.":"タ", 
    "---":"レ",
    "---.":"ソ",
    ".--.":"ツ", 
    ".--.":"ネ",
    ".-.":"ナ",
    "...":"ラ",
    "-":"ム", 
    "..-":"ウ",
    ".-..-":"ヰ",
    "..--":"ノ", 
    ".-...":"オ",
    "...-":"ク", 
    ".--":"ヤ",
    ".--.":"マ",
    "-.--":"ケ",
    "--..":"フ",
    "----":"コ", 
    "-.---":"エ",
    ".-.--":"テ",
    "--.--":"ア", 
    "-.-.-":"サ",
    "-.-..":"キ", 
    ".--..":"ユ",
    ".---.":"メ",
    "..-.-":"ミ", 
    "--.-.":"シ",
    ".--..":"ヱ",
    "--..-":"ヒ",
    "-..-.":"モ",
    ".---.":"セ", 
    "---.-":"ス",
    ".-.-.":"ン",
    "..":"゛", 
    "..--.":"゜",
    ".--.-":"ー", 
    ".-.-..":"、"
}

if (type == 1):
    morse_dict = english_morse_dict
else:
    morse_dict = japanese_morse_dict

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
                    try:
                        type_letter = morse_dict[morse]

                        morse_output = morse_output + type_letter

                        if (type == 2):
                            type_nihongo(type_letter) #Pyautogui isn't able to put Japanese letters so using function "type_nihongo." (nihongo means Japanese in Japanese)
                            morse = ""
                        else:
                            pyautogui.write(type_letter)
                            morse = ""
                    except:
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

    

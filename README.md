# Morse-keyboard
Japanese Version（日本語版)は[こちら](README-JA.md)
## Overview

The software converts Morse code (CW) to keyboard input by using buttons or keys (any switch that can be turned on and off) connected to the Arduino as the input device. Speeds, etc. can be switched within the code.

## Installation

To make this program work, the following four things are required.

1. write telegraph.ino to the Arduino Uno
2. connect a button or an electric key to digital pin 2 of the Arduino Uno
3. install the necessary libraries in Python
4. start the Python program

### Computer side

This program was created using Arduino IDE and Python 3.11. The Arduino code should be written to Arduino Uno using Arduino IDE. There are no special libraries required. The Python program requires the PySerial, Pyperclip, and Pyautogui libraries to be installed.

```
pip install pyautogui
pip install pyserial
pip install pyperclip
```

Change "COM4" on line 15 in the program to match your environment. The numbers can be checked from within the Arduino IDE. Refer to the picture.

![Arduino-IDE](/arduino-ide.jpg) 

### Arduino Side

Verification has been done only with Arduino Uno. Other Arduino has not been tested.

Connect an electric key or tact switch(In the extreme, two wires can be used. You can turn it on and off by connecting and disconnecting the wires. I don't suggest it though), etc. to the two digital pins of the Arduino Uno. The pin number should be specified in the first line of [telegraph.ino](telegraph.ino). The default is set to 2.

## Change Speed

If you want to change the length of the Morse long point, change the "speed" variable on line 6 on "receiver.py." This should be entered as the length of the long point in seconds. Also, the "space_speed" variable on line 7 is the length of whitespace (space between words). This, too, should be entered as the length of the space in seconds.

## Switch between Japanese and European (Roman Letters) Morse

You can switch between Japanese and Latin modes by changing the settings. To switch, change the "type" variable on line 14 of "Receiver.py." If the value is set to 1, the mode is set to European mode; if the value is set to 2, the mode is set to Japanese mode. I want to add Korean mode if possible.

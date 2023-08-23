# Morse-keyboard
## 概要

**ENGLISH VERSION IS [HERE](README.md)!!!**

Arduinoを使用し、電鍵をキーボード化するソフトウェアです。Arduinoに接続されたボタンまたは電鍵など（ONとOFFの切り替えができるスイッチであればなんでも可）を入力装置とし、モールス信号（CW）をキーボード入力に変換します。スピードなどは、コード内で切り替えることができます。

## インストール

本プログラムを動作させるには、次の4つのことが必要です。

1. telegraph.inoのArduino Unoへの書き込み
2. Arduino Unoのデジタルピン２にボタンや電鍵を接続
3. Pythonで必要なライブラリをインストール
4. Pythonプログラムを起動

## PC側

本プログラムは、Arduino IDE及びPython 3.11を使用し作成されました。Arduinoのコードは、Arduino IDEを用いてArduino Unoに書き込んでください。特に必要なライブラリ等はありません。また、PythonプログラムはPySerialライブラリ、Pyperclipライブラリ、Pyautoguiライブラリのインストールが必要です。

```
pip install pyautogui
pip install pyserial
pip install pyperclip
```

プログラム内の１５行目の「COM4」は、環境に合わせて変更してください。数字の部分は、Arduino IDE内から確認が可能です。写真を参照してください。

## Arduino Uno側

検証はArduino Unoでのみ行っております。他のArduinoは未検証です。

Arduino Unoのデジタルピン2ピンに、電鍵またはタクトスイッチなどを接続してください。ピン番号は、telegraph.inoの一行目で指定してください。デフォルトは２に設定されています。


![Arduino-IDE](/arduino-ide.jpg) 

## 速度変更

モールスの長点の長さを変更したい場合は、Receiver.pyの６行目の「speed」変数を変更してください。これは、長点の長さを秒数で入力してください。また、７行目の「space_speed」変数は、空白の長さ（語と語のスペース）です。これも、空白の長さを秒数で入力してください。

## モールスの和文・欧文切り替え

設定を変更することで、和文モード・欧文モードと切り替えることができます。切り替えるには、Receiver.pyの14行目の「type」変数を変更してください。値を1に設定すると、欧文モードになり、2に設定すると和文モードになります。

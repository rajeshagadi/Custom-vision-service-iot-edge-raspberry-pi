import  /home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD
from Adafruit_CharLCD import  Adafruit_CharLCD
import time
from enum import Enum

class DisplayManager(object):
    def __init__(self):
        self.s=Adafruit_CharLCD()
        self.s.clear()
        self.__displayText("Welcome")
        time.sleep(1)
        self.s.clear()

    def __displayText(self, strText):
        self.s.message(strText)

    def displayText(self, strText):
        print("Displaying " + strText)
        if 'none' not in strText.lower():
            self.__displayText(strText)
        elif 'none' in strText.lower():
            self.s.clear()
        else:
            self.__displayText("Unknown!")
            self.s.clear()


# Note - script will only run on Raspberry-Pi 
# or an OS capable of installing the RPi.GPIO package.

import RPi.GPIO as GPIO
import time
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from guimech import Ui_main

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Setting pin modes
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(22, GPIO.OUT)
# GPIO.setup(6, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)

class _vars:
    zSpeed = 0.997
    zPos = 0
    zTravel = 0
    
class guiProg(Ui_main):

    # PyQt form items
    def __init__(self, dialog):
        Ui_main.__init__(self)
        self.setupUi(dialog)
        self.jogZplus.setAutoRepeatInterval(_vars.zSpeed)
        self.jogZminus.setAutoRepeatInterval(_vars.zSpeed)
        self.jogZplus.pressed.connect(self.pulseF)
        self.jogZminus.pressed.connect(self.pulseR)
        self.setZhome.pressed.connect(self.setHome)
        self.setZdist.pressed.connect(self.setTravel)
        self.pushButton_22.pressed.connect(self.clearAll)

    # sending a forward-rotation pulse using pins 13 and 6    
    def pulseF(self):
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        _vars.zPos = _vars.zPos + 1

    # sending a reverse-rotation pulse using pins 13 and 6    
    def pulseR(self):
        GPIO.output(13, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        _vars.zPos = _vars.zPos - 1

    # setting home position.    
    def setHome(self):
        _vars.zPos = 0
        self.homeInsertLED.setEnabled(True)
        self.textBox.setText("HOME HAS BEEN RESET TO ZERO")
        
    def setTravel(self):
        _vars.zTravel = _vars.zPos
        self.jogZminus.setEnabled(False)
        self.jogZplus.setEnabled(False)
        self.setZhome.setEnabled(False)
        self.label_9.setEnabled(True)
        self.textBox.setText("THE TRAVEL HAS BEEN SET TO " + str(_vars.zTravel) + " PULSES")
             
    def clearAll(self):
        _vars.zTravel=0
        _vars.zPos=0
        self.jogZminus.setEnabled(True)
        self.jogZplus.setEnabled(True)
        self.setZhome.setEnabled(True)
        self.homeInsertLED.setEnabled(False)
        self.label_9.setEnabled(False)
        self.textBox.setText("ALL SETTINGS HAVE BEEN CLEARED")

    def runTest(self):
        while True:
            GPIO.output(13, GPIO.LOW)
            for x in range(0, _vars.zTravel):
                GPIO.output(6, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH)
                mseconds(_vars.zSpeed)
                
            GPIO.output(13, GPIO.HIGH)
            for x in range(0, _vars.zTravel):
                GPIO.output(6, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH)
                mseconds(_vars.zSpeed)       
def main():
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = guiProg(dialog)
    dialog.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()

import pifacecad
from time import sleep
import threading


class Barrier():
    def __init__(self, n):
        self.count = 0
        self.n = n

    def wait(self):
        self.count +=1
        while self.count < self.n:
            sleep(0.0001)


threading.Barrier = Barrier


class importReader():
    def __init__(self, cad=None):
        self.multiplier = 1
        self.value = 2
        self.questionmsg = None
        if cad is None:
            self.cad = pifacecad.PiFaceCAD()
            self.cad.lcd.backlight_on()
            self.cad.lcd.clear()
        self.cad = cad
        self.submitwait = None

    def setmultiplier(self, multiplier):
        self.multiplier = multiplier

    def increaseby10(self):
        print("Increasing by 10")
        self.value += (self.multiplier * 10)
        self.refreshdisplay()

    def decreaseby10(self):
        print("Decreasing by 10")
        self.value -= (self.multiplier * 10)
        if self.value < 0:
            self.value = 0
        self.refreshdisplay()

    def increaseby1(self):
        print("Increasing by 1")
        self.value += self.multiplier
        self.refreshdisplay()

    def decreaseby1(self):
        print("Decreasing by 1")
        self.value -=(self.multiplier)
        if self.value < 0:
            self.value = 0
        self.refreshdisplay()

    def submitbutton(self):
        self.submitwait.wait()


    def refreshdisplay(self):
        self.cad.lcd.clear()
        self.cad.lcd.set_cursor(0,0)
        self.cad.lcd.write(self.questionmsg)
        self.cad.lcd.set_cursor(0,1)
        self.cad.lcd.write(self.value)


    def getInput(self, questionmsg):
        self.questionmsg = questionmsg
        self.cad.lcd.clear()
        self.cad.lcd.backlight_on()
        self.cad.lcd.set_cursor(0,0)
        self.cad.lcd.write(questionmsg)
        self.cad.lcd.set_cursor(0,1)
        self.cad.lcd.write(self.value)
        listener = pifacecad.SwitchEventListener(self.cad)
        listener.register(0, pifacecad.IODIR_ON, self.increaseby1)
        listener.register(1, pifacecad.IODIR_ON, self.decreaseby1)
        listener.register(2, pifacecad.IODIR_ON, self.submitbutton)
        print("Buttons were registered")
        self.submitwait = Barrier(2);
        listener.activate
        self.submitwait.wait()
        listener.deactivate
        return self.value





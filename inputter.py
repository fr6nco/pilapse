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
        self.value = 0
        self.questionmsg = None
        if cad is None:
            self.cad = pifacecad.PiFaceCAD()
            self.cad.lcd.backlight_on()
            self.cad.lcd.clear()
        self.cad = cad
        self.submitwait = None

    def setmultiplier(self, multiplier):
        self.multiplier = multiplier

    def increaseby10(self, event=None):
        print("Increasing by 10")
        self.value += (self.multiplier * 10)
        self.refreshdisplay()

    def decreaseby10(self, event=None):
        print("Decreasing by 10")
        self.value -= (self.multiplier * 10)
        if self.value < 0:
            self.value = 0
        self.refreshdisplay()

    def increaseby1(self, event=None):
        print("Increasing by 1")
        self.value += self.multiplier
        self.refreshdisplay()

    def decreaseby1(self, event=None):
        print("Decreasing by 1")
        self.value -=(self.multiplier)
        if self.value < 0:
            self.value = 0
        self.refreshdisplay()

    def increasemultiplier(self, event=None):
        self.multiplier *= 10

    def decreasemultiplier(self, event=None):
        if (self.multiplier / 10) <= 0:
            self.multiplier = 1
        else:
            self.multiplier /= 10


    def submitbutton(self, event=None):
        self.submitwait.wait()

    def refreshdisplay(self):
        self.cad.lcd.set_cursor(0,1)
        self.cad.lcd.write(repr(self.value).rjust(10))

    def getInput(self, questionmsg):
        self.questionmsg = questionmsg
        self.value = 0
        self.cad.lcd.clear()
        self.cad.lcd.backlight_on()
        self.cad.lcd.set_cursor(0,0)
        self.cad.lcd.write(questionmsg)
        self.refreshdisplay()
        listener = pifacecad.SwitchEventListener(self.cad)
        listener.register(3, pifacecad.IODIR_ON, self.increaseby10)
        listener.register(2, pifacecad.IODIR_ON, self.increaseby1)
        listener.register(1, pifacecad.IODIR_ON, self.decreaseby1)
        listener.register(0, pifacecad.IODIR_ON, self.decreaseby10)
        listener.register(4, pifacecad.IODIR_ON, self.submitbutton)
        listener.register(6, pifacecad.IODIR_ON, self.increasemultiplier)
        listener.register(5, pifacecad.IODIR_ON, self.decreasemultiplier)
        print("Buttons were registered")
        self.submitwait = threading.Barrier(2);
        listener.activate()
        self.submitwait.wait()
        listener.deactivate()
        return self.value





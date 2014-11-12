import pifacecad

class importReader():
    def __init__(self, cad=None):
        self.multiplier = 1
        self.value = 0
        if cad is None:
            self.cad = pifacecad.PiFaceCAD()
            self.cad.lcd.backlight_on()
            self.cad.lcd.clear()
        self.cad = cad

    def setMultiplier(self, multiplier):
        self.multiplier = multiplier

    def increaseby10(self):
        self.value += (self.multiplier * 10)

    def decreaseby10(self):
        self.value -= (self.multiplier * 10)
        if self.value < 0:
            self.value = 0

    def increaseby1(self):
        self.value +=(self.multiplier)

    def decreaseby1(self):
        self.value -=(self.multiplier)
        if self.value < 0:
            self.value=0

    def getInput(self, questionmsg):
        self.cad.lcd.write(questionmsg)
        self.cad.lcd.set_cursor(0,1)
        self.cad.lcd.write("0")
        listener = pifacecad.SwitchEventListener(self.cad)
        listener.register(7, pifacecad.IODIR_ON, self.increaseby1)
        listener.register(6, pifacecad.IODIR_ON, self.decreaseby1)
        listener.activate

        listener.deactivate






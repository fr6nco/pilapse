import os
import uuid
from time import sleep

class capturer():
    def __init__(self, vid, camera, cad):
        self.vid = vid
        self.progress = 0
        self.camera = camera
        self.cad = cad
        self.directory = '/home/pi/timelapse/'
        self.foldername = ""

    def setHomeDir(self, dir):
        self.directory = dir

    def createFolder(self, name):
        os.mkdir(self.directoryname + name)

    def getFullpath(self):
        return self.directory + self.foldername

    def updateprogressbar(self, index, maxchars=16):
        self.cad.lcd.clear()
        segments = int(round((index / self.vid.getNumphotos()) * maxchars))
        self.cad.lcd.write("  Progress: ")
        self.cad.lcd.set_cursor(0,1)
        for i in range (0, segments):
            self.cad.lcd.write("#")

    def startcapture(self):
        self.foldername = uuid.uuid4();
        self.createFolder(self.foldername)
        for i in range (0, self.vid.getNumphotos):
            self.camera.capture(self.getFullpath() + "/image" + i.zfill(6) + ".jpg");
            self.updateprogressbar(i)
            sleep(self.vid.getInterval)

        return self.getFullpath()







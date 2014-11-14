import os
import uuid
from time import sleep
import string

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
        os.chdir(self.directory)
        os.mkdir(name)

    def getFullpath(self):
        return self.directory + self.foldername

    def updateprogressbar(self, index, maxchars=16):
        print("about to to calculate segments")
        segments = int(round((index / self.vid.getNumphotos()) * maxchars))
        if self.progress < segments:
            self.cad.lcd.clear()
            self.progress = segments
            self.cad.lcd.write("  Progress: ")
            self.cad.lcd.set_cursor(0,1)
            print("in update after setcursor")
            for i in range (0, segments):
                self.cad.lcd.write("#")

    def startcapture(self):
        self.foldername = str(uuid.uuid4());
        self.createFolder(self.foldername)
        os.chdir(self.foldername)
        for i in range (0, self.vid.getNumphotos()):
            print("Saving file to :" + self.getFullpath() + "/image" + str(i).zfill(6) + ".jpg")
            self.camera.capture("image" + str(i).zfill(6) + ".jpg")
            self.updateprogressbar(i)
            sleep(self.vid.getInterval())

        return self.getFullpath()







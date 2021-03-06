import vidsettings
import picamera
import pifacecad
import os
from inputter import importReader
from captureImages import capturer
from time import sleep
import subprocess

cad = pifacecad.PiFaceCAD()
camera = picamera.PiCamera()
vsettings = vidsettings.vidSettings()
inthread = importReader(cad)
val = inthread.getInput("Interval in seconds")
print(val)
vsettings.setInterval(val)
inthread.setmultiplier(100)
val = inthread.getInput("# of photos")
print(val)
vsettings.setNumphotos(val)
print(vsettings.getExectime())

cad.lcd.clear()
cad.lcd.write("Capture time:")
cad.lcd.set_cursor(0,1)
cad.lcd.write("{:3.2f}".format(vsettings.getExectime() / 60) + " minutes")
sleep(5)
cad.lcd.clear()

cap = capturer(vsettings, camera, cad)
folder = cap.startcapture()
print('Files are saved in ' + folder)
cad.lcd.clear()
cad.lcd.write("Images saved")
sleep(3)
os.chdir(folder)
cad.lcd.clear()
cad.lcd.write("Generating video")
subprocess.call('/usr/bin/ffmpeg -r 25 -i ' + folder + '/image%06d.jpg -qscale 2 ' + folder + '/output.mp4', shell=True)

cad.lcd.clear()
cad.lcd.write("output.mp4 ready")
sleep(3)
cad.lcd.clear()
exit()






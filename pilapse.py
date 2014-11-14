import vidsettings
import picamera
import pifacecad
from inputter import importReader
from captureImages import capturer
from time import sleep

cad = pifacecad.PiFaceCAD()
camera = picamera.PiCamera()
vsettings = vidsettings.vidSettings()
inthread = importReader(cad)
val = inthread.getInput("Interval in seconds")
print(val)
vsettings.setInterval(val)
inthread.setmultiplier(10)
val = inthread.getInput("# of photos")
print(val)
vsettings.setNumphotos(val)
print(vsettings.getExectime())

cad.lcd.clear()
cad.lcd.write("Capture time:")
cad.lcd.set_cursor(0,1)
cad.lcd.write( "{:3.2f}".format(vsettings.getExectime() / 60) + " minutes")
sleep(5)
cad.lcd.clear()

cap = capturer(vsettings, camera, cad)
folder = cap.startcapture()

print("Files are saved in folder : "  + folder)






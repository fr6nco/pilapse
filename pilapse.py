import vidsettings
import picamera
import pifacecad
import inputter

cad = pifacecad.PiFaceCAD()
vsettings = vidsettings.vidSettings()
inthread = inputter.importReader()
inthread.getInput("Specify picture interval in seconds")


print(vsettings.getExectime())


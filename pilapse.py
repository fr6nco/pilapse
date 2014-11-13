import vidsettings
import picamera
import pifacecad
import inputter

cad = pifacecad.PiFaceCAD()
vsettings = vidsettings.vidSettings()
inthread = inputter.importReader(cad)
val = inthread.getInput("Interval ms")
print(val)

print(vsettings.getExectime())


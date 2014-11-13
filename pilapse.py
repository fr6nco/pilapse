import vidsettings
import picamera
import pifacecad
import inputter

cad = pifacecad.PiFaceCAD()
vsettings = vidsettings.vidSettings()
inthread = inputter.importReader(cad)
val = inthread.getInput("Interval ms")
print(val)
vsettings.setInterval(val)
inthread.setmultiplier(10)
val = inthread.getInput("# of photos")
print(val)
vsettings.setNumphotos(val)

print(vsettings.getExectime())


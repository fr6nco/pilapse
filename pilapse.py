import vidsettings
import pifacecad
import picamera
import inputter

vsettings = vidsettings.vidSettings()
cad = pifacecad.PiFaceCAD()
vsettings.setInterval(5)
vsettings.setNumphotos(10)

inputter.importReader(cad, vsettings)


print(vsettings.getExectime())


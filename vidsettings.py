class vidSettings:
    def __init__(self):
        self.interval = 0
        self.numphotos = 0
        self.exectime = 0

    def getInterval(self):
        return self.interval

    def setInterval(self, value):
        self.interval = value
        self.exectime = value * self.numphotos

    def getNumphotos(self):
        return self.numphotos

    def setNumphotos(self, value):
        self.numphotos = value
        self.exectime = value * self.interval

    def getExectime(self):
        return self.exectime

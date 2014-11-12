import threading

class importReader(threading.Thread):
	def __init__(self, cad, vsettings):
		threading.Thread.__init__(self)
		self.instance = instance

	def run(self):
		print("thread started")

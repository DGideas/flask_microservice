import time
import json
__author__ = 'DGideas'
# 2016-08-17
# Python 3 with Flask

class request:
	def __init__(self):
		self.res = {}
		self.res["rst_version"] = "1.0"
		self.res["rst_time"] = time.time()
		self.res["rst_help"] = "dgideas@outlook.com"
	
	def add_param(self, param, content=None):
		if content==None:
			try:
				del self.res[param]
			except:
				pass
			return True
		else:
			self.res[param] = content
	
	def response(self):
		return json.dumps(self.res)

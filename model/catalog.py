class ClsCatalog(object):
	"""docstring for ClsCatalog"""
	def __init__(self,id,name):
		super(ClsCatalog, self).__init__()
		self.id = "cata_" + bytes(id)
		self.name = name
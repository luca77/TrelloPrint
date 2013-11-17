


class CheckItem(object):
	"""docstring for CheckItem"""
	def __init__(self, jitem):
		super(CheckItem, self).__init__()
		self.name = jitem["name"]
		self.state = jitem["state"]


	def print_me(self):
		if self.state == "complete" :
			print "[v]",
		else :
			print "[ ]",

		print self.name

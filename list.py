


class List(object):
	"""docstring for List"""
	def __init__(self, jlist, all_cards):
		super(List, self).__init__()
		self.id = jlist["id"]
		self.name = jlist["name"]
		self.closed = jlist["closed"]
		self.cards = []
		for c in all_cards :
			if (c.idList == self.id) :
				self.cards.append(c)


	def print_me(self, all='no'):
		if (all == 'no') and (self.closed == True) :
			return
		print self.name
		for c in self.cards :
			c.print_me()


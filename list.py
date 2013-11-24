

class List(object):
    """docstring for List"""
    def __init__(self, jlist, all_cards):
        super(List, self).__init__()
        self.id = jlist["id"]
        self.name = jlist["name"]
        self.closed = jlist["closed"]
        self.cards = []
        for c in all_cards:
            if (c.idList == self.id):
                self.cards.append(c)

    def __repr__(self):
        return "List()"


    def __str__(self):
        if (self.closed):
            return ""
        string = self.name + "\n"
        for c in self.cards:
            string += c + "\n"
        return string

from checklist import CheckList
from card import Card
from list import List


class Board(object):
    """docstring for Board"""
    def __init__(self, jboard):
        super(Board, self).__init__()
        self.name = jboard["name"]
        self.desc = jboard["desc"]
        self.url = jboard["url"]
        #self.labels = jboard["labelNames"]

        self.checklists = {}
        for i in jboard["checklists"]:
            x = CheckList(i)
            self.checklists[x.id] = x

        self.cards = []
        for x in jboard["cards"]:
            c = Card(x, self.checklists)
            self.cards.append(c)

        self.lists = []
        for l in jboard["lists"]:
            x = List(l, self.cards)
            self.lists.append(x)

    def print_me(self):
        print((self.name))
        print((self.url))
        if (self.desc):
            print((self.desc))
        for l in self.lists:
            l.print_me()

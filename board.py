from checklist import CheckList
from card import Card
from list import List


class Board(object):
    """docstring for Board"""
    def __init__(self, jboard):
        super(Board, self).__init__()
        self.__name = jboard["name"]
        self.__desc = jboard["desc"]
        self.__url = jboard["url"]
        #self.labels = jboard["labelNames"]

        self.__checklists = {}
        for i in jboard["checklists"]:
            x = CheckList(i)
            self.__checklists[x.id] = x

        self.__cards = []
        for x in jboard["cards"]:
            c = Card(x, self.__checklists)
            self.__cards.append(c)

        self.__lists = []
        for l in jboard["lists"]:
            x = List(l, self.__cards)
            self.__lists.append(x)

    def __str__(self):
        string = self.__name + "\n" + self.__url + "+\n"
        if (self.__desc):
            string += self.__desc + "\n"
        for l in self.__lists:
            string += str(l)
        return string

    def get_md(self):
        string = "# " + self.__name + "\n\n" + self.__url + "\n\n"
        if (self.__desc):
            string += self.__desc + "\n\n"
        for l in self.__lists:
            string += l.get_md()
        return string
from utility import print_bg


class Card(object):
    """docstring for Card"""

    def __init__(self, jcard, checklist):
        super(Card, self).__init__()
        self.name = jcard["name"]
        self.desc = jcard["desc"]
        self.idList = jcard["idList"]
        self.labels = {}
        for l in jcard["labels"]:
            self.labels[l["color"]] = l["name"]
        self.cl = {}
        for i in jcard["idChecklists"]:
            self.cl[i] = checklist[i]

    def print_me(self):
        print()
        print((self.name))
        if (self.desc):
            print((self.desc))
        for l in list(self.labels.keys()):
            print_bg(self.labels[l], l)

        for i in sorted(self.cl.keys()):
            self.cl[i].print_me()
        print()

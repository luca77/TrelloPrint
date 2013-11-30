

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

    def __str__(self):
        string = self.name + "\n"
        if (self.desc):
            string += self.desc + "\n"
        for l in list(self.labels.keys()):
            string += self.labels[l] + "\n"
        for i in sorted(self.cl.keys()):
            string += str(self.cl[i]) + "\n"
        return string

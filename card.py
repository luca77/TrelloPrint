

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
            label = ""
            if (self.labels[l]):
                label = self.labels[l]
            else:
                label = l
            string += label + "\n"
        for i in sorted(self.cl.keys()):
            string += str(self.cl[i]) + "\n"
        return string

    def get_md(self):
        string = "### " + self.name + "\n\n"
        if (self.desc):
            string += self.desc + "\n\n"
        if (self.labels):
            string += "**Labels**: "
            for l in list(self.labels.keys()):
                label = ""
                if (self.labels[l]):
                    label = self.labels[l]
                else:
                    label = l
                string += "\"" + label + "\" "
            string += "\n\n"
        for i in sorted(self.cl.keys()):
            string += self.cl[i].get_md()
        return string + "\n"

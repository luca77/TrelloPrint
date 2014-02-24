

class Card(object):
    """docstring for Card"""

    def __init__(self, jcard, checklist):
        super(Card, self).__init__()
        self.__name = jcard["name"]
        self.__desc = jcard["desc"]
        self.__idList = jcard["idList"]
        self.__labels = {}
        for l in jcard["labels"]:
            self.__labels[l["color"]] = l["name"]
        self.__cl = {}
        for i in jcard["idChecklists"]:
            self.__cl[i] = checklist[i]

    def __str__(self):
        string = self.__name + "\n"
        if (self.__desc):
            string += self.__desc + "\n"
        for l in list(self.__labels.keys()):
            label = ""
            if (self.__labels[l]):
                label = self.__labels[l]
            else:
                label = l
            string += label + "\n"
        for i in sorted(self.__cl.keys()):
            string += str(self.__cl[i]) + "\n"
        return string

    def get_md(self):
        string = "### " + self.__name + "\n\n"
        if (self.__desc):
            string += self.__desc + "\n\n"
        if (self.__labels):
            string += "**Labels**: "
            for l in list(self.__labels.keys()):
                label = ""
                if (self.__labels[l]):
                    label = self.__labels[l]
                else:
                    label = l
                string += "\"" + label + "\" "
            string += "\n\n"
        for i in sorted(self.__cl.keys()):
            string += self.__cl[i].get_md()
        return string + "\n"

    def get_list_id(self):
        return self.__idList

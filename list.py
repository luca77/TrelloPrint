

class List(object):
    """docstring for List"""
    def __init__(self, jlist, all_cards):
        super(List, self).__init__()
        self.__id = jlist["id"]
        self.__name = jlist["name"]
        self.__closed = jlist["closed"]
        self.__cards = []
        for c in all_cards:
            if (c.get_list_id() == self.__id):
                self.__cards.append(c)

    def __str__(self):
        if (self.__closed):
            return ""
        string = "====================\n" + self.__name + "\n"
        for c in self.__cards:
            string += "--------------------\n" + str(c) + "\n"
        return string

    def get_md(self):
        if (self.__closed):
            return ""
        string = "## " + self.__name + "\n\n"
        for c in self.__cards:
            string += c.get_md()
        return string + "\n"
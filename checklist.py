from checkitem import CheckItem


class CheckList(object):
    """docstring for CheckList"""
    def __init__(self, jlist):
        super(CheckList, self).__init__()
        self.id = jlist["id"]
        self.name = jlist["name"]
        self.list = {}
        for j in jlist["checkItems"]:
            x = CheckItem(j)
            self.list[j["pos"]] = x

    def print_me(self):
        print((self.name))
        for j in sorted(self.list.keys()):
            self.list[j].print_me()

from checkitem import CheckItem


class CheckList(object):
    """docstring for CheckList"""
    def __init__(self, jlist):
        super(CheckList, self).__init__()
        self.__id = jlist["id"]
        self.__name = jlist["name"]
        self.__list = {}
        for j in jlist["checkItems"]:
            x = CheckItem(j)
            self.__list[j["pos"]] = x

    def __str__(self):
        string = self.__name + "\n"
        for j in sorted(self.__list.keys()):
            string += str(self.__list[j])
        return string

    def get_md(self):
        string = "#### " + self.__name + "\n\n"
        for j in sorted(self.__list.keys()):
            string += "- " + str(self.__list[j])
        return string + "\n\n"

    def get_id(self):
        return self.__id

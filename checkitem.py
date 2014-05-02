

class CheckItem(object):

    """docstring for CheckItem"""

    def __init__(self, jitem):
        super(CheckItem, self).__init__()
        self.__name = jitem["name"]
        self.__state = jitem["state"]

    def __str__(self):
        string = ""
        if self.__state == "complete":
            string += "[v] "
        else:
            string += "[ ] "
        return string + self.__name + "\n"

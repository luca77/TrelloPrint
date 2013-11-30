

class CheckItem(object):
    """docstring for CheckItem"""
    def __init__(self, jitem):
        super(CheckItem, self).__init__()
        self.name = jitem["name"]
        self.state = jitem["state"]

    def __str__(self):
        string = ""
        if self.state == "complete":
            string += "[v] "
        else:
            string += "[ ] "
        return string + self.name + "\n"

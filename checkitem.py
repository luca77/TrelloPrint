

class CheckItem(object):
    """docstring for CheckItem"""
    def __init__(self, jitem):
        super(CheckItem, self).__init__()
        self.name = jitem["name"]
        self.state = jitem["state"]

    def print_me(self):
        if self.state == "complete":
            print("[v]", end=' ')
        else:
            print("[ ]", end=' ')

        print(self.name)

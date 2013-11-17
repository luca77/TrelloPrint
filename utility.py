

def print_bg(msg, color):
    color_table = {
        'orange': 208,
        'red': 1,
        'yellow': 11,
        'green': 2,
        'purple': 56,
        'blue': 4
    }
    CSI = "\x1B["
    color = CSI + "48;5;" + str(color_table[color]) + "m"
    reset = CSI + "0m"
    print((color + msg + reset))


def print_c(msg, color):
    standard = '\033[0m'
    code = standard

    if color == 'dark_grey':
        code = '\033[90m'
    elif color == 'red':
        code = '\033[91m'
    elif color == 'yellow':
        code = '\033[93m'
    elif color == 'green':
        code = '\033[92m'
    elif color == 'blue':
        code = '\033[94m'
    elif color == 'pink':
        code = '\033[95m'
    elif color == 'light_blue':
        code = '\033[96m'
    elif color == 'white':
        code = '\033[97m'

    print((code + msg + standard))

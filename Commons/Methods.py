def display_mini(self, s):
    self.mini_log.setText(s)

def display(s):
    print(s)


red_background = "QLabel { background-color : red; color : white;}"
green_background = "QLabel { background-color : green; color : white;}"
orange_background = "QLabel { background-color : orange; color : white;}"


def choice_back(i):
    i = int(i)
    if i % 2 == 0:
        ch = red_background
    else:
        ch = green_background
    return ch

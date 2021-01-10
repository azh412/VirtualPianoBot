import pyautogui, time, random
choice = input("Song name: ")
time.sleep(1.75)
class Song:
    def __init__(self, reg, new, dash, name):
        self.reg = reg # Regular gap between notes (sec)
        self.new = new # Newline gap between notes (sec)
        self.dash = dash # Gap for dash separated notes (sec)
        self.name = name # Name of song
w = [
    Song(0.12, 0.5, None, "holiday"),
    Song(0.08, None, None, "pirate"),
    Song(0.21, None, None, "terimeri"),
    Song(0.16, 1, 0.05, "christmas"),
    Song(0.1, 0.27, None, "coffin"),
    Song(0.13, None, None, "goldenwind"),
    Song(0.18, 0.03, None, "snowman"),
    Song(0.17, 0.25, 0.04, "office"),
    Song(0.2, None, 0.03, "avengers"),
    Song(0.24, None, None, "birthday"),
    Song(0.16, None, None, "rocketeer"),
    Song(0.18, 0.25, 0.1, "furelise"),
    Song(0.21, None, None, "unknown"),
    Song(0.22, None, None, "seeyouagain"),
    Song(0.13, None, 0.0150, "chariots"),
    Song(0.22, None, None, "happier")
]

for o in w:
    if o.name == choice:
        with open(f"sheets/{o.name}.txt", "r") as text:
            f = text.readlines()
            for a in f:
                if o.new != None:
                    if a == '\n' == None:
                        time.sleep(o.new)
                for i in a.split():
                    if o.dash != None:
                        if i == '-':
                            time.sleep(o.dash)
                            continue
                    pyautogui.typewrite(i)
                    time.sleep(o.reg)
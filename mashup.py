import pyautogui, time, random
time.sleep(2)
class Song:
    def __init__(self, reg, new, dash, name):
        self.reg = reg
        self.new = new
        self.dash = dash
        self.name = name
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
    Song(0.13, None, 0.0150, "chariots")
]
for i in range(3):
    random.shuffle(w)
for o in w:
    with open(f"sheets/{o.name}.txt", "r") as text:
        f = text.readlines()
        for a in f:
            if o.new:
                if a == '\n':
                    time.sleep(o.new)
            for i in a.split():
                if o.dash:
                    if i == '-':
                        time.sleep(o.dash)
                        continue
                pyautogui.typewrite(i)
                time.sleep(o.reg)

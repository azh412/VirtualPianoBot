import pyautogui, time, random, keyboard
from termcolor import colored
print(colored("sheet name: ", "green"), end="")
choice = input()

class Song:
    def __init__(self, reg, new, dash, name, desc):
        self.reg = reg # Regular gap between notes (sec)
        self.new = new # Newline gap between notes (sec)
        self.dash = dash # Gap for dash separated notes (sec)
        self.name = name # Name of song
        self.desc = desc # Real name and artist(s)

w = [
    Song(0.12, 0.5, None, "holiday", "Holiday by Lil Nas X"),
    Song(0.08, None, None, "pirate", "He's A Pirate by Klaus Badelt"),
    Song(0.21, None, None, "terimeri", "Teri Meri by Shreya Ghosal and Rafat Fateh Ali Khan"),
    Song(0.16, 1, 0.05, "christmas", "All I Want For Christmas Is You by Mariah Carey"),
    Song(0.1, 0.27, None, "astronomia", "Astronomia by Vicetone and Tony Igy"),
    Song(0.13, None, None, "goldenwind", "Golden Wind from JoJo's Bizzare Adventure"),
    Song(0.18, 0.03, None, "snowman", "Do You Want To Build A Snowman by Kristen Anderson-Lopez and Robert Lopez"),
    Song(0.17, 0.25, 0.04, "office", "The Office Theme Song"),
    Song(0.2, None, 0.03, "avengers", "The Avengers Infinity War Theme"),
    Song(0.24, None, None, "birthday", "Happy Birthday"),
    Song(0.18, 0.25, 0.1, "furelise", "Fur Elise by Ludwig Van Beethoven"),
    Song(0.21, None, None, "unknown", "Into the Unknown by Idina Menzel"),
    Song(0.22, None, None, "seeyouagain", "See You Again by Wiz Khalifa"),
    Song(0.13, None, 0.0150, "chariots", "Chariots of Fire by Vangelis"),
    Song(0.22, None, None, "happier", "Happier by Marshmello")
]


for o in w:
    if o.name == choice:
        print(colored(f"Press the Esc key to start playing {o.desc}!", "yellow"))
        while True:
            if keyboard.is_pressed("esc"):
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
                            if keyboard.is_pressed("esc"):
                                exit(0)
                            time.sleep(o.reg)
                    exit(0)        
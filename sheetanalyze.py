# Copyright (c) 2021 Azhaan Salam
# Licensed under the MIT License

from termcolor import colored

print(colored("sheet name: ", "green"), end="")
inp = input()

file = []
has = 2
with open(f"sheets/{inp}.txt", "r") as f:
    j = f.readlines()
    for i in j:
        for x in i.split():
            for l in x:
                if l == '[':
                    has = 1
                    break
            x = x.strip("-")        
            if has == 2 and len(x) > 1:
                x = ' - '.join(x[i:i + 1] for i in range(0, len(x), 1))
            x = x.strip("[")
            x = x.strip(']')
            x = x.replace("|", "\n\n")
            file.append(x)
            has = 2

with open(f"sheets/{inp}.txt", "w") as f:
    f.truncate(0)

with open(f"{inp}.txt", "a") as f:
    for i in range(6):
        f.write("\n")
    for i in file:
        f.write(i)
        f.write(" ")    

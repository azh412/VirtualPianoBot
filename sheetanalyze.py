inp = input("sheet name: ")
file = []
has = 0
with open(f"{inp}.txt", "r") as f:
    j = f.readlines()
    for i in j:
        for x in i.split():
            for l in x:
                if l == '[':
                    has = 1
            if has == 0 and len(x) > 1:
                x = ' - '.join(x[i:i + 1] for i in range(0, len(x), 1)) 
            x = x.strip("[")
            x = x.strip(']')
            x = x.replace("|", "\n\n")
            file.append(x)
            has = 0
with open(f"{inp}.txt", "a") as f:
    for i in range(6):
        f.write("\n")
    for i in file:
        f.write(i)
        f.write(" ")    
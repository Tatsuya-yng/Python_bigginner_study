r = open("sample.txt", "r", encoding="UTF-8")
for line in r:
    print(line, end="")
r.close()
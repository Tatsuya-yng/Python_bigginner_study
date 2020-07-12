
r = open('sample.txt', 'r', encoding='utf-8')
data = r.readlines()
for line in data:
    print(line, end="")
r.close()

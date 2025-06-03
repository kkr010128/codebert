r = []
while True:
    line = input()
    if line == '0':
        break
    r.append(sum([int(s) for s in line]))

for s in r:
    print(s)
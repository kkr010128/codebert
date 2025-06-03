res = []
while True:
    s = input()
    if s == '0':
        break

    res.append(sum([int(x) for x in s]))

for e in res:
    print(e)
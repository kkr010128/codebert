W = input().strip().upper()
T = []
while True:
    t = input().strip().split()
    if t[0] == 'END_OF_TEXT':
        break
    else:
        for i in t:
            T.append(i.upper())

print(T.count(W))
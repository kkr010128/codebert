W = input().upper()
T = []
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    T += [x.upper() for x in t.split()]
print(T.count(W))

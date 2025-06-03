H, A = (int(x) for x in input().split())

if A >= H:
    print(1)
elif H%A == 0:
    print(H//A)
else:
    print(H//A + 1)
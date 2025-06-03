n = int(input())
tarou = 0
hanako = 0
for i in range(n):
    w1, w2 = input().split()
    if w1 == w2:
        tarou += 1
        hanako += 1
    elif w1 > w2:
        tarou += 3
    else:
        hanako += 3

print(tarou, hanako)
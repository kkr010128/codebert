n = map(int, input().split(" "))
for index, i in enumerate(n, 1):
    if i == 0:
        print(index)
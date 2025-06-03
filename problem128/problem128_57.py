x, n = map(int, input().split())
p = list(map(int, input().split()))

for i in range(1000):
    if x-i not in p:
        print(x-i)
        exit()
    elif x+i not in p:
        print(x+i)
        exit()
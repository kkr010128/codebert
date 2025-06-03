x, n = map(int, input().split())
p = list(map(int, input().split()))

i = 0
while True:
    if x-i not in p:
        print(x-i)
        break
    if x+i not in p:
        print(x+i)
        break
    i += 1
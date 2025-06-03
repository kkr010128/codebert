a, b = map(int, input().split())

i = 1
while True:
    x = a * i
    if x % b == 0:
        print(x)
        exit()
    i += 1

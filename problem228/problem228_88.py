h = [int(input())]
a = 1
while(True):
    if h[0] < 1:
        break
    h = list(map(lambda x: x / 2, h))
    a = a * 2
print(a - 1)

A = int(input())
B = int(input())

for x in range(1, 4):
    if x not in [A, B]:
        print(x)
        break

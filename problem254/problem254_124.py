A = int(input())
B = int(input())
for i in range(1, 4):
    if i in [A, B]:
        continue
    else:
        print(i)
        break
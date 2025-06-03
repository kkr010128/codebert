n = int(input())
s = 0
b = False
for _ in range(n):
    w = input().split()
    if w[0] == w[1]:
        s += 1
        if s == 3:
            b = True
            break
    else:
        s = 0
print('Yes' if b else 'No')

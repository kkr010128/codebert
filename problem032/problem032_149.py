import math
n = int(input())
x, y = [int(e) for e in input().split()], [int(e) for e in input().split()]
D1 = D2 = D3 = 0; D4 = []
for x1, y1 in zip(x, y):
    D1 += abs(x1-y1)
    D2 += abs(x1-y1)**2
    D3 += abs(x1-y1)**3
    D4.append(abs(x1-y1))
print('{0:.6f}'.format(D1))
print('{0:.6f}'.format(math.sqrt(D2)))
print('{0:.6f}'.format(math.pow(D3, (1/3))))
print('{0:.6f}'.format(max(D4)))


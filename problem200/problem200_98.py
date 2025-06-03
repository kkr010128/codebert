A, B, M = map(int, input().split())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
m = []


for n in range(M):
    m.append([int(s) for s in input().split()])

minValue = min(a) + min(b)

for i in range(M):
    discountPrice = a[m[i][0] - 1] + b[m[i][1] - 1] - m[i][2]
    if discountPrice  < minValue:
        minValue = discountPrice

print(minValue)

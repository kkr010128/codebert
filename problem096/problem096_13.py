import math

in1 = list(map(int,input().split()))
Nin = in1[0]
Din = in1[1]

xy = [map(int, input().split()) for _ in range(Nin)]
x, y = [list(i) for i in zip(*xy)]

count=0

for i in range(Nin):
    dist = math.sqrt(x[i]**2 + y[i]**2)
    if dist <= Din:
        count += 1

print(count)

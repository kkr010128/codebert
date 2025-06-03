import math

n = input()
x = [int(_) for _ in raw_input().split()]
y = [int(_) for _ in raw_input().split()]

for p in range(1,4):
    sum = 0
    for i in range(n):
        sum += math.pow(abs(x[i] - y[i]),p)
    print math.pow(sum,1/float(p))

print max([abs(float(i) - float(j)) for i,j in zip(x,y) ])
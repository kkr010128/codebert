import math
n = int(raw_input())
x = map(lambda l: int(l)*1.0, (raw_input()).split(" "))
y = map(lambda l: int(l)*1.0, (raw_input()).split(" "))

for p in range(1,4):
    d = [math.pow(math.fabs(x[i] - y[i]), p) for i in range(n)]
    print math.pow(sum(d), 1.0/p)

d = [math.fabs(x[i]-y[i]) for i in range(n)]
print max(d)
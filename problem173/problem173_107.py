import math
N = int(input())
total = N/2*(N+1)

f = math.floor(N/3)
f = (3*f+3)*f/2
b = math.floor(N/5)
b = (5*b+5)*b/2
fb = math.floor(N/15)
fb = (15*fb+15)*fb/2

print(int(total-f-b+fb))

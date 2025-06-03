import math

num = int(input())

x = list(map(float,input().split()))

y = list(map(float,input().split()))

diff = [0]*num

for a in range(num):
    diff[a] = abs(x[a] - y[a])
    
print(sum(diff)) #1

po = [0]*num

for b in range(num):
    po[b] = diff[b] * diff[b]
    
print(math.sqrt(sum(po))) #2



for c in range(num):
    po[c] = diff[c] * diff[c] * diff[c]
    
print((sum(po))**(1/3)) #3

_max = 0

for d in diff:
    if _max < d:
        _max = d

print(_max)#infinity

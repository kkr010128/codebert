import math
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

D1 = 0
d2 = 0
d3 = 0
dm =[]
for i in range(n):
    D1 += abs(x[i]-y[i])
    d2 += (abs(x[i]-y[i]))**2
    d3 += (abs(x[i]-y[i]))**3
    m = abs(x[i]-y[i])
    dm.append(m)
    
D2 = math.sqrt(d2)
D3 = d3 ** (1/3)
Dm = max(dm) 

print(f'{D1:.06f}')
print(f'{D2:.06f}')
print(f'{D3:.06f}')
print(f'{Dm:.06f}')

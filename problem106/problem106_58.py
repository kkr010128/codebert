from sys import stdin
inp = lambda : stdin.readline().strip()

n = int(inp())
a = [0]*10**5
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            a[i**2 + j**2 + k**2 + i*j + i*k + k*j] += 1
for i in a[1:n+1]:
    print(i) 
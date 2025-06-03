n = int(input())
x = list(map(int,input().split()))
ans = 100**2 * n

for i in range(1,101):
    energy = 0
    for j in x:
        energy += (i-j)**2
    ans = min(ans, energy)

print(ans)
N=int(input())
X=list(map(int, input().split()))

power_min = 1e8
for P in range(1,101):
    power = 0
    for i in range(N):
        power += (X[i]-P)**2
    if power < power_min:
        power_min = power

print(power_min)
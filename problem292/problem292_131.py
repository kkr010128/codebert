N = int(input())
D = list(map(int,input().split()))
power = 0
for i in range(N-1):
    for j in range(i+1,N):
        power += D[i]*D[j]
print(power)


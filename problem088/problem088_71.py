N = int(input())
A = list(map(int, input().split()))

humidai = [0]*N
s = A[0]

for i in range(1, N):
    if A[i]<s:
        humidai[i]=s-A[i]
    else:
        s = A[i]

print(sum(humidai))

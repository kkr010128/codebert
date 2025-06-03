N = int(input())
P = list(map(int,input().split()))
num = 1
min_P = P[0]
for i in range(1,N):
    if P[i] < min_P:
        min_P = P[i]
        num += 1
print(num)
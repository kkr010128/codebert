N = int(input())
a = list(map(int,input().split()))
S = 0
for i in range(N):
    S ^= a[i]

Ans = ""
for i in range(N):
    print(S^a[i])
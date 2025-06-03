import sys
input = sys.stdin.readline

n=int(input())
L=list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans += L[i]*L[j]
print(ans)


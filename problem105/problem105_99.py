N = int(input())
ans = 0
A = list(map(int, input().split()))
for a in A[::2]:
    if a%2 != 0:
        ans += 1
        
print(ans)
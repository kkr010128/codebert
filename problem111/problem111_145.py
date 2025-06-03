N = int(input())
A = sorted([int(x) for x in input().split()], reverse=True)


ans = 0
for i in range(N):
    if i == 0:
        continue
    else:
        ans += A[i//2]
print(ans)

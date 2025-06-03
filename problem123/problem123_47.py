def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
a = inputlist()

xor = 0
for i in range(N):
    xor = xor ^ a[i]

ans = [0]*N
for i in range(N):
    ans[i] = a[i]^xor
print(*ans)
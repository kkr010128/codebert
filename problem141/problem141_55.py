N = int(input())
A = [int(i) for i in input().split()]

L, R = [A[-1]], [A[-1]]
for i in range(1, N+1):
    L.append((L[-1]+1)//2+A[-1-i])
    R.append((R[-1]+A[-1-i]))
L = L[::-1]
R = R[::-1]

if L[0] >= 2:
    print(-1)
    exit()

ans = 1
p = 1
for i in range(1, N+1):
    ans += min(p*2, R[i])
    p = min(p*2, R[i])-A[i]
print(ans)

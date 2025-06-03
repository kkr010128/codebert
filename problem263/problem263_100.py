from collections import deque
N = int(input())
A = deque(map(int, input().split()))
mod = 10**9 + 7
M = len(bin(max(A))) - 2
ans = 0
bitlist = [1]
anslist = [0 for _ in range(M)]
for k in range(M):
    bitlist.append(bitlist[-1]*2%mod)
counter = [0 for _ in range(M)]

for k in range(N):
    a = A.pop()
    c = 0
    while a:
        b = a & 1
        if b == 0:
            anslist[c] += counter[-c-1]
        else:
            anslist[c] += k - counter[-c-1]
            counter[-c-1] += 1
        c += 1
        a >>= 1
    while c < M:
        anslist[c] += counter[-c-1]
        c += 1
for k in range(M):
    ans += anslist[k]*bitlist[k]%mod
    ans %= mod
print(ans)

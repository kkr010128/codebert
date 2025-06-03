N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
D = {}
for a in A:
    bit = bin(a)[2:][::-1]
    for i in range(len(bit)):
        if bit[i] == '1':
            if i not in D:
                D[i] = 1
            else:
                D[i] += 1

ans = 0
for k, v in D.items():
    ans += (N-v)*v*2**k % mod
    ans = ans % mod

print(ans)
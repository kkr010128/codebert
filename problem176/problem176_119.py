N, K = map(int, input().split())
ans = 0
mod = 10 ** 9 + 7
count = [0] * (K+10)
for i in range(K,0,-1):
    t = pow(K//i, N, mod)
    j = 2
    while j * i <= K:
        t -= count[j*i]
        j += 1
    count[i] = t
    # tがiの倍数からなる数列の個数であることが確定しているはず
    ans += t * i
    ans %= mod

print(ans)

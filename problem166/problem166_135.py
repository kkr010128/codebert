from collections import Counter

S = input()
N = len(S)
mod = [0] * (N+1)
now = 0
for i in range(N):
    now += int(S[N-1-i]) * pow(10,i,2019) % 2019
    now %= 2019
    mod[N-i-1] = now

ans = 0
for l in Counter(mod).values():
    ans += l * (l-1) // 2
print(ans)
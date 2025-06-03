D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]

last = [0]*26
ans = 0
for d in range(D):
    max_s = int(input()) - 1
    last[max_s] = d+1
    ans += s[d][max_s]
    for i in range(26):
        ans -= (c[i]*(d+1 - last[i]))
    print(ans)
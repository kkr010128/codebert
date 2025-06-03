N, P = map(int, input().split())
S = input()

ans = 0
if P == 2 or P == 5 :
    for i in range(N) :
        if int(S[i])%P == 0 :
            ans += i+1
    print(ans)
    exit()

modP = [0 for _ in range(P)]
modP[0] = 1
now = 0
t = 1
for i in range(N) :
    now += int(S[-1-i]) * t
    now %= P
    modP[now] += 1
    t = t * 10 % P

for r in modP :
    ans += r*(r-1)//2

print(ans)

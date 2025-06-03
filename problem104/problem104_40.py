L, R, d = input().split()
L = int(L)
R = int(R)
d = int(d)
cnt = 0
for t in range(L,R+1):
    if t % d == 0:
        cnt = cnt + 1

print(cnt)

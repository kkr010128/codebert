import sys
input = sys.stdin.readline

N = int(input())
S = [input()[:-1] for _ in range(N)]
high = []
low = []
for i in range(N):
    cnt = 0
    m = 0
    for j in range(len(S[i])):
        if S[i][j] == "(":
            cnt += 1
        else:
            cnt -= 1
        m = min(m, cnt)
    if cnt > 0:
        high.append([m, cnt])
    else:
        low.append([m-cnt, -cnt])
high.sort(reverse=True)
low.sort(reverse=True)

h = 0
for m, up in high:
    if h+m < 0:
        print("No")
        sys.exit()
    h += up
p = 0
for m, down in low:
    if p+m < 0:
        print("No")
        sys.exit()
    p += down
if h == p:
    print("Yes")
else:
    print("No")



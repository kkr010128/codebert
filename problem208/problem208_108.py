import sys
n,m = map(int, input().split())
num = [0]*n
al = [-1]*n
Ans = 0
for i in range(m):
    s,c = map(int, input().split())
    if num[s-1] != 0 and num[s-1] != c:
        print(-1)
        sys.exit()
    else:
        num[s-1] = c
        al[s-1] = c
if al.count(0)==n and n >= 2:
    print(-1)
    sys.exit()
if al[0] == 0and n >= 2:
    print(-1)
    sys.exit()
if num[0] == 0 and n >= 2:
    num[0] = 1
for i in range(len(num)):
    Ans = Ans + num[i] * (10 ** (n-i-1))

if Ans == 0 and n >= 2:
    print(-1)
else:
    print(Ans)
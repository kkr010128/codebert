import sys
N,M = map(int,input().split())
s = [0] * M
c = [0] * M
a = ["-1"] * (N)
if N == 1 and M == 0:
    print(0)
    sys.exit()
for i in range(M):
    s[i],c[i] = map(int,input().split())

for j in range(M):
    if s[j] == 1 and c[j] == 0 and N != 1:
        print(-1)
        sys.exit()
    elif a[s[j]-1] == "-1":
        a[s[j]-1] = str(c[j])
    elif a[s[j]-1] == str(c[j]):
        pass
    else:
        print(-1)
        sys.exit()
if a[0] == "-1":
    a[0] = "1"
for h in range(1,N):
    if a[h] == "-1":
        a[h] = "0"
ans = "".join(a)
print(int(ans))
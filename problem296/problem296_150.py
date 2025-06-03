s = input()
k = int(input())

if len(s) == 1:
    print(k//2)
    exit()

rep = [1]
prev = s[0]
for i in range(1, len(s)):
    if s[i] == prev:
        rep[-1] += 1
    else:
        rep.append(1)
        prev = s[i]

if len(rep) == 1:
    print(rep[0]*k//2)
    exit()

cnt = 0
for r in rep:
    cnt += r//2

if s[0] == s[-1]:
    ans = cnt*k + ((rep[0]+rep[-1])//2 - rep[0]//2 - rep[-1]//2)*(k-1)
    print(ans)
else:
    print(cnt*k)

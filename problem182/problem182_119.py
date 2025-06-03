n, k, c = map(int, input().split())
s = list(str(input()))

def getpos(s):
    l = []
    i = 0
    while i <= n-1 and len(l) < k:
        if s[i] == 'o':
            l.append(i)
            i += c+1
        else:
            i += 1
    return l

l = getpos(s)

s.reverse()
r = getpos(s)
for i in range(len(r)):
    r[i] = n-1-r[i]

#print(l)
#print(r)

lastl = [-1]*(n+1)
lastr = [-1]*(n+1)

for i in range(k):
    lastl[l[i]+1] = i

for i in range(n):
    if lastl[i+1] == -1:
        lastl[i+1] = lastl[i]

for i in range(k):
    lastr[r[i]] = i

for i in reversed(range(n)):
    if lastr[i] == -1:
        lastr[i] = lastr[i+1]

#print(lastl)
#print(lastr)

ans = []
s.reverse()
for i in range(n):
    if s[i] != 'o':
        continue
    cnt = 0
    cnt += lastl[i]+1
    cnt += lastr[i+1]+1
    if lastl[i] != -1 and lastr[i+1] != -1 and r[lastr[i+1]] - l[lastl[i]] <= c:
        cnt -= 1
    if cnt < k:
        ans.append(i+1)

for i in range(len(ans)):
    print(ans[i])
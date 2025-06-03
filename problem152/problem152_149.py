from bisect import bisect
N = int(input())
S = [input() for _ in range(N)]

def count(s):
    n = len(s)
    n1 = 0
    n2 = 0
    for i in range(n):
        if s[i]=='(':
            n2 += 1
        else:
            if n2 > 0:
                n2 -= 1
            else:
                n1 += 1
    return n1,n2

l1 = []
l2 = []
m1 = 0
m2 = 0
for i in range(N):
    n1,n2 = count(S[i])
    if n1+n2==0:
        continue
    if n1 == 0:
        m1 += n2
        continue
    if n2 == 0:
        m2 += n1
        continue
    if n2-n1>=0:
        l1.append([n1,n2])
    else:
        l2.append([n1,n2])

ans = 'Yes'
l1.sort()
for i in range(len(l1)):
    n1,n2 = l1[i]
    if m1 < n1:
        ans = 'No'
        break
    m1 += n2-n1

l2.sort(key=lambda x:x[1])
for i in range(len(l2)):
    n1,n2 = l2[i]
    if m2 < n2:
        ans = 'No'
        break
    m2 += n1-n2

if m1!=m2:
    ans = 'No'

print(ans)


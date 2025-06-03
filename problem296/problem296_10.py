import copy
s = list(input())
n = len(s)
s2 = copy.deepcopy(s)
la = s[-1]
for i in range(n):
    if s[i] == la:
        s2.append(la)
    else:
        break

n2 = len(s2)
k = int(input())
if n2 == 2*n:
    print(n*k//2)
    exit()
count = 0
for i in range(n2-n+1,n2):
    if s2[i] == s2[i-1]:
        s2[i] = "1"
        count += 1
ans = k*count

c = 0

for i in range(n-1,-1,-1):
    if la == s[i]:
        c += 1
    else:
        break

if n2 > n and (n2-n)%2 and c > 1 and c%2:
    ans -= 1
print(ans)
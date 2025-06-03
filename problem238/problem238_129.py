n,k,s = map(int,input().split())
rem = s+1
if rem > 10**9:
    rem = 1
li = []
for i in range(n):
    if i < k:
        li.append(s)
    else:
        li.append(rem)
print(*li)

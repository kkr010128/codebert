n = int(input())
a = list(map(int,input().split()))
if a == [1]*n:
    print("pairwise coprime")
    quit()
m = max(a)
l = [-1]*(m+3)
for i in range(2,m+1):
    if l[i] != -1:
        continue
    l[i] = i
    j = 2
    while i*j <= m:
        if l[i*j] == -1:
            l[i*j] = i
        j += 1
def fastfact(i,lst):
    if l[i] == -1:
        return lst
    while i > 1:
        lst.append(l[i])
        i //= l[i]
    return lst
check = [0]*(m+1)
for i in range(n):
    if a[i] == 1:
        continue
    s = set(fastfact(a[i],[]))
    for j in s:
        check[j] += 1
M = max(check)
if M == 1:
    print("pairwise coprime")
elif M == n:
    print("not coprime")
else:
    print("setwise coprime")
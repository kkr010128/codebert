def inp():
    return input()
def iinp():
    return int(input())
def inps():
    return input().split()
def miinps():
    return map(int,input().split())
def linps():
    return list(input().split())
def lmiinps():
    return list(map(int,input().split()))
def lmiinpsf(n):
    return [list(map(int,input().split()))for _ in range(n)]

n = iinp()
l = lmiinps()

ans = 0

if n < 3:
    print(0)
    exit()

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if l[i] == l[j] or l[j] == l[k] or l[i] == l[k]:
                continue
            if l[i]+l[j] > l[k] and l[j]+l[k] > l[i] and l[k]+l[i] > l[j]:
                ans += 1

print(ans)
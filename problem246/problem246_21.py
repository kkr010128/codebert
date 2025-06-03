# C - Count Order
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
L = []

def rec(l,s):
    if len(l)==N:
        L.append(l)
    else:
        for x in s:
            tmp_l = l[:]
            tmp_l.append(x)
            tmp_s = s[:]
            tmp_s.remove(x)
            rec(tmp_l,tmp_s)

rec(list(),[i+1 for i in range(N)])

a = 0
while P!=L[a]:
    a += 1
b = 0
while Q!=L[b]:
    b += 1
print(abs(a-b))
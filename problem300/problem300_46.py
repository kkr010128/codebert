A, B = map(int,input().split())
P = [1]
a = set([1,A])
b = set([1,B])
for k in range(2,2+int(max(A,B)**(1/2))):
    if A%k == 0 and B%k == 0:
        P.append(k)
        a.add(A//k)
        b.add(B//k)
    elif A%k == 0:
        a.add(A//k)
    elif B%k == 0:
        b.add(B//k)

P += list(a&b)
P.sort()
U = set([])
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
for e in P:
    flag = 1
    for used in U:
        if gcd(e,used) != 1:
            flag = 0
            break
    if flag == 1:
        U.add(e)
print(len(U))

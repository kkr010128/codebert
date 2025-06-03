import collections

def U1(a,b):
    if b > a:
        b, a = a, b
    while a%b != 0:
        r = a%b
        a = b
        b = r
    return b

K = int(input())
c = 0
arr = []

for i in range(1,K+1):
    for j in range(1,K+1):
        arr.append(U1(i,j))

arr=collections.Counter(arr)

for key,value in arr.items():
    for k in range(1,K+1):
        c += U1(k,key)*value

print(c)
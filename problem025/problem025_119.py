n = int(input())
a = list(map(int,input().split()))
b = [2 ** i for i in range(n)]
c = {}
for i in range(2 ** n):
    k = 0
    k += i
    v = 0
    for j in range(n)[::-1]:
        v += k // b[j] * a[j]
        k %= b[j]
    c[v] = 0
m = int(input())
a = list(map(int,input().split()))
for i in range(m):
    try:
        c[a[i]]
        print("yes")
    except:
        print("no")
    

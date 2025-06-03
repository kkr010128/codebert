n,k = input().split()
n = int(n)
k = int(k)
a = [True for i in range(n)]

while k>0:
    d = int(input())
    b = input().split()
    for e in b:
        a[int(e)-1] = False
    k-=1
print(sum(a))
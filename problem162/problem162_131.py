def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

n,m=n1()

if n%2==0:
    if m>=2:
        e=n//2
        s=1
        l=e-s
        c=0
        while e>s and c<m:
            print(s,e)
            s+=1
            e-=1
            c+=1
        e=n
        s=n-l+1
        while e>s and c<m:
            print(s,e)
            s+=1
            e-=1
            c+=1
    else:
        print(1,2)
else:
    if m>=2:
        e=n//2+1
        s=1
        l=e-s
        c=0
        while e>s and c<m :
            print(s,e)
            s+=1
            e-=1
            c+=1
        e=n
        s=n-l+1
        while e>s and c<m:
            print(s,e)
            s+=1
            e-=1
            c+=1
    else:
        print(1,2)
n=int(input())
a=list(map(int,input().split()))
suma=sum(a)
f=0
p=suma-2*f
for i in a:
    f+=i
    p=min(p,abs(suma-2*f))
print(p)
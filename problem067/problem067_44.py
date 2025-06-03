n=int(input())
a=0
b=0
for i in range(n):
    c,d=input().split()
    if c<d:
        b+=3
    elif c>d:
        a+=3
    else:
        b+=1
        a+=1
print(a,b)

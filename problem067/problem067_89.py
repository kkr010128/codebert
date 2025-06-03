t=0
h=0
for i in range(int(input())):
    A,B=list(input().split())
    if A>B:
        t+=3
    if A<B:
        h+=3
    if A==B:
        t+=1
        h+=1
print(t,h)

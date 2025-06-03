n=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    s+=i**2
print(int(((sum(d))**2)/2-(s/2)))
n=int(input())
i=1
c=0
while(n>=1):
    c+=i
    i*=2
    n//=2
print(c)

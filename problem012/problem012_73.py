def isprime(x):
    if  x==2:
        return True
    if x<2 or x&1==0:
        return False
    return pow(2,x-1,x)==1

cnt=0
n=int(input())
for i in range(n):
    a=int(input())
    if isprime(a):
        cnt+=1
print(cnt)
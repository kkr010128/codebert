#C
A,B=map(int,input().split())
GCD=1
for i in range(2,10**5+1):
    if A%i==0 and B%i==0:
        GCD=i

LCM=A*B/GCD
print(int(LCM))
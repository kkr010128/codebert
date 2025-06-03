n=int(input())
a=0
b=0
while n!=0:
    n=n//2
    a+=2**b
    b+=1
print(a)
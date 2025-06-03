n=int(input())

a=1
b=1

while n:
    a,b=b,a+b
    n -=1
    
print(a)

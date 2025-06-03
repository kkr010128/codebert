def isPrime(x):
    if x==2:
        return True
    
    if x<2 or x%2==0:
        return False
    
    for n in range(3,int(x**0.5)+1,2):
        if x%n==0:
            return False
    return True   

n=int(input())
num=[int(input()) for i in range(n)]

i=0
for nm in num:
    if isPrime(nm):
        i+=1
        
print(i)
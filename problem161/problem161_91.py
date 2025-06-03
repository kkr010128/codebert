a,b,n = list(map(int,input().split()))
if n < b :
    x = n
else :
    x = b-1
    
print(a*x//b-a*(x//b))
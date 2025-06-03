import math
john=[]
while True:
    try:
        john.append(input())
    except EOFError:
        break
for i in john:
    k=list(map(int,i.split()))
    print(int(math.gcd(k[0],k[1])),int(k[0]*k[1]/math.gcd(k[0],k[1])))
    
    

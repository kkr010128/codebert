n  = int(input())

ren = 0

for i in range(n):

     a, b = (int(x) for x in input().split())

     if a == b:
        ren += 1 

     elif ren >= 3:
         continue
    
     else: 
        ren = 0

if ren >= 3:
    print("Yes")
    
else:
    print("No")
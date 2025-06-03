X=int(input())
 
x=100
for i in range(10**4):
    x += x//100
    if X <= x:
        print(i+1)
        break
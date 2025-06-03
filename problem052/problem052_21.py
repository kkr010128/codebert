import math

x = int(input())
for i in range(1,x+1):
    if i%3==0:
        print(f" {i}",end="")
        continue
    r=i
    while True:
        if r<=0:
            break
        if r%10==3:
            print(f" {i}",end="")
            break
        r//=10
print("")


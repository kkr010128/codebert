a=int(input())
b=0
c=int(a**(1/2))
for i in range(-1000,1000):
    for j in range(-1000,1000):
        if((i**5)-(j**5)==a):
            b=1
            break
    if(b==1):
        break
print(i,j)
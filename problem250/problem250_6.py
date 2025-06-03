x=int(input())
while 1:
    for i in range(2,x):
        if x%i==0:
            x+=1
            break
    else:
        break
print(x)
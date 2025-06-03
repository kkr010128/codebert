k=int(input())
num=7
i=1
while True:
    if k%2==0 or k%5==0:
        i=-1
        break
    num%=k
    if num==0:
        break
    else:
        num*=10
        num+=7
        i+=1
print(i)
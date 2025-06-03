n=int(input())
t=0
flag=False
for i in range(1,10):
    for j in range(1,10):
        if n==i*j:
            print('Yes')
            t+=1
            flag=True
            break
    if flag:
        break

if t==0:
    print('No')
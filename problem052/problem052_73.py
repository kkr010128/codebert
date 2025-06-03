a=[]
n=int(input())
i=1
c=0
while i <= n:
    if c==0:
        x=i
        if x%3==0:
            a.append(i)
            i+=1
            continue
    c=0
    if x%10==3:
        a.append(i)
        i+=1
        continue
    x//=10
    if x == 0:
        i+=1
        continue
    else:
        c=1
print(' ', end='')
print(*a)
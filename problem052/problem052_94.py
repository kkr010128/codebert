n=int(input())
a,c,i=[],0,1
while i <= n:
    if c==0:
        x=i
        if x%3==0:
            print(' '+str(i), end='')
            i+=1
            continue
    c=0
    if x%10==3:
        print(' '+str(i), end='')
        i+=1
        continue
    x//=10
    if x == 0:
        i+=1
        continue
    else:
        c=1
print()
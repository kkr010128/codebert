import sys
x=[]
n=input()
for i in range(3,n+1):
    if i%3==0:
        x.append(i)
    else:
        j=i
        while j!=0:
            if j%10==3:
                x.append(i)
                break
            j=j/10

X=iter(x)
for i in X:
    sys.stdout.write(' ')
    sys.stdout.write('%d'%i)
print('')
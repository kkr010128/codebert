def fibonum():
    global F
    F[0]=1
    F[1]=1
    for i in xrange(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]

n=input()
F=[0]*(n+1)
num=fibonum()
print(num)
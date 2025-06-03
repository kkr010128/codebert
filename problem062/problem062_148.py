x = 1
L=[]
n= 0
s=0
while x is not 0:
    x = int(input())
    L.append(x)
N=1
L.remove(0)
for i in L:
    while i >=N:

        N=10*N
        n =i%N
        s+=(n/N*10)
        i-=n
    print (int(s))
    s=0
    N = 1
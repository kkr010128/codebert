NX = input().split()
n = int(NX[0])
x = int(NX[1])

while n!=0 or x!=0:
    out = 0
    for ii in range(n-2):
        i = ii+1 #i:1~n-2
        for jj in range(n-1-i):
            j = jj+1+i #j:i+1~i+1+n-2-i=i+1~n-1
            for kk in range(n-j):
                k = kk+1+j #k:j+1~n-j+j+1 =
                if k !=i and k!=j and i+j+k == x:
                    out = out+1
    print(out)
    NX = input().split()
    n = int(NX[0])
    x = int(NX[1])
import numpy
N,M,X = map(int,input().split())
A = numpy.array([[int(i) for i in input().split()] for _ in range(N)])
ans = 10**8
for i in range(2**N) :
    i = format(i,'b').zfill(N)
    check = numpy.array([0]*(M+1))
    for j in range(N) :
        if i[j] == '0' :
            continue
        check +=  A[j][0:]
    if all (check[m] >= X for m in range(1,M+1)) :
        ans = min(ans,check[0])

if ans == 10**8 :
    print(-1)
else :
    print(ans)
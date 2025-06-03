import sys
N,M = map(int,input().split())


if N%2 == 1:
    for i in range(1,M+1):
        print(i,N-i+1)

elif N%4 == 0:
    total = 0
    count = 1
    for i in range(N//4,0,-1):
        print(i,i+count)
        count += 2
        total += 1
        if total >= M:
            sys.exit()
    count = 2
    for i in range(3*(N//4)-1,N//2,-1):
        print(i,i+count)
        count += 2
        total += 1
        if total >= M:
            sys.exit()
else:
    total = 0
    count = 1
    for i in range(N//4,0,-1):
        print(i,i+count)
        count += 2
        total += 1
        if total >= M:
            sys.exit()
    count = 2
    for i in range(3*(N//4),N//2-1,-1):
        print(i,i+count)
        count += 2
        total += 1
        if total >= M:
            sys.exit()
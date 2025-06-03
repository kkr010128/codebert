# import time

N,P = list(map(int,input().split()))
S = input()

if P == 2:
    c = 0
    for i in range(N):
        u = int(S[i])
        if u % 2 == 0:
            c += i+1
    print(c)
        
elif P == 5:
    c = 0
    for i in range(N):
        u = int(S[i])
        if u % 5 == 0:
            c += i+1
    print(c)

else:
    U = [0]
    a = 0
    t = 1
    
    for i in range(N):
        t %= P
        a += int(S[-i-1])*t
        a %= P
        t *= 10
        U.append(a)
    U.append(10001)
    # print(U)
    
    # t3 = time.time()
    
    c = 0
    
    """
    for i in range(P):
        m = U.count(i)
        c += m*(m-1)//2
    print(c)
    """
    U.sort()
    # print(U)
    idx = 0
    q = -1
    for i in range(N+2):
        if q != U[i]:
            q = U[i]
            m = i - idx
            idx = i
            c += m*(m-1)//2
    print(c)
    # t4 = time.time()
    # print(t4-t3)
    
    # 10032
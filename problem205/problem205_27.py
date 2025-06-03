N,P = map(int,input().split())
S = list(map(int,list(input())))
if P==2:
    cnt = 0
    for i in range(N):
        if S[i]%2==0:
            cnt += i+1
elif P==5:
    cnt = 0
    for i in range(N):
        if S[i]==0 or S[i]==5:
            cnt += i+1
else:
    A = [0 for _ in range(N)]
    a = 0
    b = 1
    for i in range(N-1,-1,-1):
        a = (a+b*S[i])%P
        A[i] = a
        b = (b*10)%P
    C = {i:0 for i in range(P)}
    for i in range(N):
        C[A[i]] += 1
    cnt = 0
    for i in range(P):
        cnt += (C[i]*(C[i]-1))//2
    cnt += C[0]
print(cnt)
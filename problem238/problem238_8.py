N,K,S=map(int,input().split())
if S==10**9:
    for i in range(K):
        print(S,"",end="")
    for i in range(K,N):
        print(1,"",end="")
    print()
else:
    for i in range(K):
        print(S,"",end="")
    for i in range(K,N):
        print(S+1,"",end="")
    print()

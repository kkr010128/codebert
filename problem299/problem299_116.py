def resolve():
    
    N=int(input())
    A=list(map(int,input().split()))

    d={}
    for i in range(N):
        d[A[i]]=i+1

    dict2=sorted(d.items())

    for i in range(N):
        print(dict2[i][1], end=" ")        


resolve()
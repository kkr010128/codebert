N=int(input())
A=["a"]
if N==1:
    print("a")
    exit()
else:
    S="abcdefghijklmn"
    slist=list(S) 
    for i in range(2,N+1):
        temp=[[] for _ in range(N)]
        for j in range(i-1):
            for w in A[j]:
                for u in slist[:j+1]:
                    temp[j].append(w+u)
                temp[j+1].append(w+slist[j+1])
        A=temp
    B=[]    
    for j in range(N):
        for t in A[j]:
            B.append(t)
    B.sort()
    for i in range(len(B)):
        print(B[i])
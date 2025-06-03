N=int(input())
L=[[10**9]for i in range(N+1)]
for i in range(N):
    l=list(map(int,input().split()))
    for j in range(l[1]):
        L[i+1].append(l[2+j])
#print(L)
for i in range(N+1):
    L[i].sort(reverse=True)
    
#print(L)
ans=[]
for i in range(N+1):
    ans.append([0,0])


from collections import deque 

Q=deque()
cnt=1
for i in range(N):
    Q.append([0,N-i])
for i in range(10**7):

    if len(Q)==0:
        break
    q0,q1=Q.pop()
    #print(q0,q1)
    if q1!=10**9:
        if ans[q1][0]==0:
            ans[q1][0]=cnt
            cnt+=1
            for j in L[q1]:
                Q.append([q1,j])
    else:
        ans[q0][1]=cnt
        cnt+=1
    #print(ans,Q)
for i in range(1,N+1):
    print(i,ans[i][0],ans[i][1])

from collections import deque
N,M=map(int,input().split())
S=input()
j=N
ans=deque()
while j>0:
    for i in range(M,0,-1):

        if j-i==0:
            ans.appendleft(i)
            print(*ans)

        elif j-i<0:
            continue
        if S[j-i]=="0":
            ans.appendleft(i)
            j-=i
            break
        if i==1 and S[j-i]=="1":
            print(-1)
            exit()

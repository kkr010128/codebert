from collections import deque
 
def main():
    H,W=map(int,input().split())
    S=[]
    for i in range(H):
        s=input()
        S.append(s)
 
    G=[]
    for i in range(H):
        for j in range(W):
            tmp=[]
            if S[i][j]=="#":
                G.append(tmp)
                continue
            if i-1>=0:
                if S[i-1][j]==".":
                    tmp.append((i-1)*W+j)
            if i+1<=H-1:
                if S[i+1][j]==".":
                    tmp.append((i+1)*W+j)
            if j-1>=0:
                if S[i][j-1]==".":
                    tmp.append(i*W+j-1)
            if j+1<=W-1:
                if S[i][j+1]==".":
                    tmp.append(i*W+j+1)
            G.append(tmp)
 
    res=0
 
    for start in range(H*W):
        dist = 0
        v = [-1 for _ in range(H * W)]
        que=deque([])
        que.append(start)
        v[start]=dist
        while len(que)>0:
            next_index=que.popleft()
            next=G[next_index]
            for i in next:
                if v[i]==-1:
                    que.append(i)
                    v[i]=v[next_index]+1
 
        if max(v)>=res:
            res=max(v)
 
    print(res)
 
 
if __name__=="__main__":
    main()
 
 
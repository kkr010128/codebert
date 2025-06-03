#

import sys
input=sys.stdin.readline

def main():
    H,W,K=map(int,input().split())
    mas=[input().strip("\n") for i in range(H)]
    mincut=H*W
    for bit in range(2**(H-1)):
        sep=[]
        for s in range(H-1):
            if (bit>>s)&1:
                sep.append(s)
        cutcnt=len(sep)
        cnt=[0]*(len(sep)+1)
        for j in range(W):
            ci=0
            cntt=cnt[:]
            for i in range(H):
                if mas[i][j]=="1":
                    cnt[ci]+=1
                if i in sep:
                    ci+=1
            if max(cnt)>K:
                for i in range(len(sep)+1):
                    cnt[i]-=cntt[i]
                cutcnt+=1
        if max(cnt)>K:
            cutcnt=10000000000
        if cutcnt<mincut:
            mincut=cutcnt
    print(mincut)
                
    
    
if __name__=="__main__":
    main()

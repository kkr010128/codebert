import sys
from collections import deque

def main():
    N,K,C=map(int,input().split())
    S=input()

    Left=deque([])
    Right=deque([])

    counter=0
    while counter<N and len(Left)<K:
        if S[counter]=="o":
            if len(Left)<K:
                Left.append(counter)
                counter+=C
        counter+=1

    counter=N-1
    while counter>=0 and len(Right)<K:
        if S[counter]=="o":
            if len(Right)<K:
                Right.appendleft(counter)
                counter-=C
        counter-=1

    if len(Right)!=K or len(Left)!=K:
        sys.exit()
    for i in range(K):
        l=Left.popleft()
        r=Right.popleft()
        if l==r:
            print(l+1)

if __name__=="__main__":
    main()
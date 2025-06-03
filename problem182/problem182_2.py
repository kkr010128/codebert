

def resolve():
    N,K,C = map(int,input().split())
    S=input()

    dpt1=[0]*K
    dpt2=[0]*K
    pnt = 0
    for i in range(K):
        while S[pnt]=="x":
            pnt+=1
        dpt1[i]=pnt
        pnt += C+1

    pnt = N-1
    for i in range(K-1,-1,-1):
        while S[pnt] == "x":
            pnt -=1
        dpt2[i]=pnt
        pnt-=C+1

    for a,b in zip(dpt1,dpt2):
        if a == b:
            print(a+1)
if __name__ == "__main__":
    resolve()
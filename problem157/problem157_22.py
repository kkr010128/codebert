#j-i=Ai+Aj(j>i)
#j-Aj=Ai+i

#Lj=Ri=X
from bisect import bisect_left

def main():
    N=int(input())
    A=list(map(int,input().split()))

    L={}
    R={}

    res=0

    for i in range(N):
        l=(i+1)-A[i]
        r=A[i]+i+1
        if (l in R.keys()):
            res+=len(R[l])
        if (r in R.keys()):
            R[r].append(i+1)
        else:
            R[r]=[i+1]


    print(res)

if __name__=="__main__":
    main()




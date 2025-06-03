def main():
    N=int(input())
    A=list(map(int,input().split()))

    L={}
    R={}

    for i in range(N):
        l=(i+1)+A[i]
        r=(i+1)-A[i]
        if (l in L.keys()):
            L[l]+=1
        else:
            L[l]=1
        if r in R.keys():
            R[r]+=1
        else:
            R[r]=1

    res=0
    for key in L.keys():
        if key in R.keys():
            res+=R[key]*L[key]

    print(res)
if __name__=="__main__":
    main()

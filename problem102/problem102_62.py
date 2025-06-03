def main():
    N,K=map(int,input().split())
    A=[0]+list(map(int,input().split()))
    for i in range(K+1,N+1):
        if A[i]>A[i-K]:
            print("Yes")
        else:
            print("No")
if __name__=='__main__':
    main()
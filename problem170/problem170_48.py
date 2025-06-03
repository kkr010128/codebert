def main():
    N,K=map(int,input().split())

    res=0

    MOD=10**9+7

    for i in range(K,N+2):
        MAX=(N+(N-i+1))*i//2
        MIN=(i-1)*i//2

        res+=MAX-MIN+1
        res%=MOD

    print(res%MOD)

if __name__=="__main__":
    main()
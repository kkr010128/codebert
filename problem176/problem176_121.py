def main():
    N,K=map(int,input().split())

    M={}

    mod=pow(10,9)+7
    res=0
    for i in range(K,0,-1):
        syou=K//i
        mc=pow(syou,N,mod)
        if syou>=2:
            for sub_m in range(2,syou+1):
                mc-=M[sub_m*i]
        res+=(i*mc)%mod
        M[i]=mc

    print(res%mod)

if __name__=="__main__":
    main()
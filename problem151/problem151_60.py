def main():
    N,M,K=map(int,input().split())
    MOD=998244353
    E=0

    n_=1
    for i in range(1,N):
        n_=(n_*i)%MOD

    nr_ = 1
    nr_array=[]
    for i in range(1,N-1):
        nr_ = (nr_ * i) % MOD
        nr_array.append(nr_)
    m=1
    Mk_array=[1]
    for i in range(1,N):
        m=(m*(M-1))%MOD
        Mk_array.append(m)
    r_=1
    for i in range(0,K+1):
        if i!=0 and i!=N-1:
            r_ = (r_ * i) % MOD
            nr_=nr_array.pop()
            power_r=pow(r_,MOD-2,MOD)
            power_nr=pow(nr_,MOD-2,MOD)
        Mk=Mk_array.pop()

        if i!=0 and i!=N-1:
            E+=(n_*power_r*power_nr*Mk)%MOD
        else:
            E+=Mk%MOD

    res=(M*E)%MOD
    print(res)

if __name__=="__main__":
    main()


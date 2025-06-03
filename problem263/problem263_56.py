def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    # Aの中でd桁目が0,1であるものの個数を求める(p,qとする)
    # 全部のd桁目についてループして、ans+=(2**d)*(p*q)
    ans = 0
    for d in range(60):
        p,q = 0,0
        for i in range(N):
            if A[i]%2==0: p+=1
            else: q+=1
            A[i] //= 2
        ans += ((2**d)*p*q)%MOD
        ans %= MOD
    print(ans)

main()

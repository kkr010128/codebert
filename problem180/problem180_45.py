def main():
    N,K = map(int,input().split())
    syo = N//K
    amari = N%K
    N = abs(amari-K)
    ans = min(N,amari)
    return ans
    

print(main())

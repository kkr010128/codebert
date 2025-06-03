def main():
    N,A,B = map(int,input().split())
    syo = N//(A+B)
    amari = N%(A+B)
    ans = syo*A
    if amari < A:
        ans += amari
    else:
        ans += A

    return ans

print(main())

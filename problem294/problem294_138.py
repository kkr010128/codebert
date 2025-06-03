def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans = 0
    for ia in range(N-2):
        a = L[ia]
        ic = ia + 2
        for ib in range(ia+1, N-1):
            b = L[ib]
            while ic < N and L[ic] < a+b:
                ic += 1
            ans += ic - (ib + 1)
    print(ans)
main()
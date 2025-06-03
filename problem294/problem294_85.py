from bisect import bisect_left

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))

    ans = 0
    for ia in range(N):
        for ib in range(ia+1, N-1):
            a = L[ia]
            b = L[ib]
            ic_end = bisect_left(L, a+b, lo=ib+1)
            ans += ic_end - (ib+1)

    print(ans)
main()
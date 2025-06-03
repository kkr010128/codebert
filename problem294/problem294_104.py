import bisect

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for a_idx in range(N-2):
        for b_idx in range(a_idx+1, N-1):
            l_idx = b_idx + 1
            r_idx = bisect.bisect_left(L, L[a_idx] + L[b_idx])
            ans += r_idx - l_idx
    print(ans)


if __name__ == '__main__':
    main()

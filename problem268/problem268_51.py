MOD = 10**9 + 7


def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0]*N
    ans = 3
    for a in A:
        if a == 0:
            if B[a] == 1:
                ans *= 2
        else:
            ans *= B[a-1] - B[a]
        B[a] += 1
        if 3 < B[a] or (a != 0 and B[a-1] < B[a]):
            ans = 0
            break
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()

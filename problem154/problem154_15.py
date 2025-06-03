if __name__ == '__main__':
    N, K = map(int, input().split())
    have_snack = []
    for i in range(K):
        n = int(input())
        have_snack.extend(list(map(int, input().split())))
    ans = N - len(set(have_snack))
    print(ans)


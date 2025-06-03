import itertools

def main():
    N = int(input())
    n_x_y = {}
    for n in range(N):
        A = int(input())
        x_y = {}
        for _ in range(A):
            x, y = map(int, input().split())
            x_y[x-1] = y
        n_x_y[n] = x_y

    ans = 0
    for flags in itertools.product([1, 0], repeat=N):
        sat = True
        for n, flag in enumerate(flags):
            if flag == 0:
                continue
            for x, y in n_x_y[n].items():
                if (y == 1 and flags[x] == 0) or (y == 0 and flags[x] == 1):
                    sat = False
                    break
            if sat is False:
                break
        if sat is True and sum(flags) > ans:
            ans = sum(flags)

    print(ans)


if __name__ == '__main__':
    main()

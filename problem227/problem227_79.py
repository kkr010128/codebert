def solve():
    N,K = [int(i) for i in input().split()]
    H = [int(i) for i in input().split()]

    if K >= len(H):
        print('0')
    else:
        sorted_H = sorted(H)
        alived = N - K
        print(sum(sorted_H[:alived]))

if __name__ == "__main__":
    solve()
from sys import stdin


def readline_from_stdin() -> str:
    return stdin.readline().rstrip


if __name__ == '__main__':
    N, K, = input().split()
    A = [int(i) for i in input().split()]
    N, K = int(N), int(K)

    for i in range(N-K):
        if A[i] < A[K+i]:
            print("Yes")
        else:
            print("No")
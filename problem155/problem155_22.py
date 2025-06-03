import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    H = [None]
    H.extend(list(map(int, input().split())))
    bad = set([])
    for _ in range(M):
        A, B = map(int, input().split())
        if H[A] > H[B]:
            bad.add(B)
        elif H[A] < H[B]:
            bad.add(A)
        else:
            bad.add(A)
            bad.add(B)
    print(N - len(bad))


if __name__ == '__main__':
    main()

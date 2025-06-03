#  --*-coding:utf-8-*--

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*(N+1)

    b = 0
    for i, a in enumerate(A):
        b += a - 1
        b %= K
        B[i+1] = b

    Q = {}
    X = 0

    for i, b in enumerate(B):
        if i>=K:
            Q[B[i-K]] -= 1

        if b in Q:
            X += Q[b]
            Q[b] += 1
        else:
            Q[b] = 1

    print(X)


if __name__ == '__main__':
    main()

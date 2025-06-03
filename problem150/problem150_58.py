#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    A = [int(x) - 1 for x in input().split()]

    way = []
    seen = [False for _ in [0] * (2 * 10 ** 5 + 1)]
    now = 0
    for _ in range(K):
        if seen[now]:
            loop_start = way.index(now)
            loop = way[loop_start:]
            K -= len(way[:loop_start])
            now = loop[K % len(loop)]
            break
        way.append(now)
        seen[now] = True
        now = A[now]
    print(now + 1)


if __name__ == '__main__':
    main()

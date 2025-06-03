def main():
    N, K, C = map(int, input().split())
    S = input()

    # greedy
    head, tail = [-C - 1] * (K + 1), [N + C + 1] * (K + 1)
    idx = 0
    for i in range(N):
        if S[i] == 'o' and i - head[idx] > C:
            idx += 1
            head[idx] = i
            if idx == K:
                break
    idx = K
    for i in range(N - 1, -1, -1):
        if S[i] == 'o' and tail[idx] - i > C:
            idx -= 1
            tail[idx] = i
            if idx == 0:
                break
    # ans
    for i in range(K):
        if head[i + 1] == tail[i]:
            print(tail[i] + 1)


if __name__ == '__main__':
    main()

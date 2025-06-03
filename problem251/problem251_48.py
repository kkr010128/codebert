def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    d = {'r': R, 's': S, 'p': P}
    T = input()
    scores = []
    for t in T:
        if t == 'r':
            scores.append('p')
        elif t == 's':
            scores.append('r')
        else:
            scores.append('s')
    for i in range(N-K):
        if scores[i] == scores[i+K]:
            scores[i+K] = 0
    print(sum([d[v] for v in scores if v in ['p', 'r', 's']]))


if __name__ == '__main__':
    main()

def main():
    N, K = map(int, input().split())
    P = map(int, input().split())
    E = [(p+1)/2 for p in P]
    sums = [sum(E[0:K])]
    for i in range(N-K):
        sums.append(sums[-1] - E[i] + E[i+K])
    print(max(sums))


if __name__ == '__main__':
    main()

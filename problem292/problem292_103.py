#!/usr/bin/env python

def main():
    N = int(input())
    d = list(map(int, input().split()))

    cumSum = [0] * N
    cumSum[0] = d[0]
    for i in range(1, N):
        cumSum[i] = cumSum[i-1] + d[i]

    ans = 0
    for i in range(N-1):
        ans += d[i] * (cumSum[N-1] - cumSum[i])

    print(ans)

if __name__ == '__main__':
    main()
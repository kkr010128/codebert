import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if M%2:
    cnt = 0
    for i in range(1, M//2 + 1):
        cnt += 1
        print(i, M + 2 - i)
        print(M + 1 + i, 2*M + 2 - i)

    i = cnt + 1
    print(i, M + 2 - i)
else:
    for i in range(1, M//2 + 1):
        print(i, M + 2 - i)
        print(M + 1 + i, 2*M + 2 - i)
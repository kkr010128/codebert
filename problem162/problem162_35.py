N,M = map(int,input().split())
if M % 2 == 1:
    for i in range(M // 2):
        print(1 + i, M - i)
    for i in range(M - M // 2):
        print(M + 1 + i, 2 * M + 1 - i)
else:
    for i in range(M // 2):
        print(1 + i, M + 1 - i)
        print(M + 2 + i, 2 * M + 1 - i)
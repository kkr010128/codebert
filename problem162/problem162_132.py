N, M = map(int, input().split())

M_f = M * 2 + 1
if M % 2 != 0:
    for i in range(0, M // 2):
        print(i + 1, (M) - i)
    for i in range(0, M // 2 + 1):
        print(M + 1 + i, M_f - i)
else:
    for i in range(0, M // 2):
        print(i + 1, (M + 1) - i)
    for i in range(0, M // 2):
        print(M + 2 + i, M_f - i)
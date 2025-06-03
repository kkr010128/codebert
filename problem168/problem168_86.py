N, M = map(int, input().split())
A = list(map(int, input().split()))
def answer(N: int, M: int, A: list) -> int:
    homework_days = 0
    for i in range(0, M):
        homework_days += int(A[i])
        i += 1
    if homework_days <= N:
        return N - homework_days
    else:
        return -1

print(answer(N, M, A))
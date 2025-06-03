N = int(input())
A = list(map(int, input().split()))

if A[0] == 1:
    if len(A) > 1:
        print(-1)
        exit()
    else:
        print(1)
        exit()
elif A[0] > 1:
    print(-1)
    exit()

S = [0] * (N + 2)
for i in range(N, -1, -1):
    S[i] = S[i + 1] + A[i]

sec = [0] * (N + 1)
sec[0] = 1
for i in range(1, N + 1):
    a = A[i]
    v = sec[i - 1] * 2
    if v < a:
        print(-1)
        exit()
    sec[i] = min(v - a, S[i + 1])

print(sum(A) + sum(sec[:-1]))
# print(sec)
# print(A)
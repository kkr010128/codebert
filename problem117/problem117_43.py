N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sumA = [0]
sumB = [0]
tmp = 0
answer = 0
st = 0

for i in range(N):
    tmp = tmp + A[i]
    sumA.append(tmp)

tmp = 0
for i in range(M):
    tmp = tmp + B[i]
    sumB.append(tmp)

for i in range(N, -1, -1):
    booktmp = 0

    for j in range(st, M + 1):

        if sumA[i] + sumB[j] <= K:
            booktmp = i + j
        else:
            st = j
            break
    answer = max(answer, booktmp)
    if j == M:
        break


print(answer)



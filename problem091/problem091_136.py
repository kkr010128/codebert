N = int(input())
L = list(map(int, input().split()))

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if L[i] != L[j]:
            for k in range(j + 1, N):
                if L[i] != L[k] and L[j] != L[k]:
                    M = [L[i], L[j], L[k]]
                    M.sort()
                    if M[2] < M[0] + M[1]:
                        cnt += 1
print(cnt)
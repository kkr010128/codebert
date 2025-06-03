N = int(input())
L = list(map(int, input().split()))

ans = 0
if N > 2:
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                tmp = [L[i], L[j], L[k]]
                if (len(tmp) == len(set(tmp))) and (L[i] + L[j] > L[k]) and (
                        L[j] + L[k] > L[i]) and (L[k] + L[i] > L[j]):
                    ans += 1
print(ans)
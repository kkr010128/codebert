N = int(input())
L = list(map(int, input().split())) #リストで複数行作るには？

count = 0

for i in range(2, N):
    for j in range(1, i):
        for k in range(0, j):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            elif L[k] < L[i] + L[j] and L[i] < L[j] + L[k] and L[j] < L[i] + L[k]:
                count += 1

print(count)
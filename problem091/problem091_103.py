N = int(input())
L = list(map(int, input().split()))
list.sort(L)
c = 0

for i in range(0, N):
        for j in range(i + 1, N):
                for k in range(j + 1, N):
                        if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                                if L[i] + L[j] > L[k]:
                                        c += 1

print(c)
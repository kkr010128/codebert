N = int(input())

L = list(map(int, input().split()))

le = len(L)

score = 0

for i in range(le):
    for j in range(i+1,le):
        for k in range(j+1,le):
            if (L[i] + L[j] > L[k] and
                L[i] + L[k] > L[j] and
                    L[k] + L[j] > L[i] ):
                         if (L[i] != L[j] and
                            L[i] != L[k] and
                            L[k] != L[j]):
                                score += 1

print(score)
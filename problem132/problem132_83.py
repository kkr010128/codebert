from itertools import accumulate

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

current_arr = A
if K > 41:
    print(*([N]*N))
    exit()
for _ in range(K):
    imos = [0] * N
    ruiseki = [0] * (N+1)
    for i, ai in enumerate(current_arr):
        imos[max([0, i-ai])] += 1
        if i+ai+1 < N:
            imos[i+ai+1] -= 1
    for j, im in enumerate(imos):
        ruiseki[j+1] = ruiseki[j] + im
    current_arr = ruiseki[1:]
#print(imos)
#print(ruiseki)
#print(*accumulate(imos))
print(*current_arr)

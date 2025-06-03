from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))

def calc_imos(arr):
    imos = [0] * (N + 1)
    for i, a in enumerate(arr):
        l = max(0, i - a)
        r = min(N - 1, i + a)
        imos[l] += 1
        imos[r + 1] -= 1
    new_arr = list(accumulate(imos))[:-1]
    return new_arr


for k in range(K):
    A = calc_imos(A)
    if all([a == N for a in A]):
        print(*([N] * N), sep=' ')
        exit()

print(*A, sep=' ')

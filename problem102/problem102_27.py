n, k = map(int, input().split())
al = list(map(int, input().split()))

for i in range(k, n):
    if al[i-k] < al[i]:
        print('Yes')
    else:
        print('No')
n, k = map(int, input().split())
scores = list(map(int, input().split()))

evals = []
cnt = 0

for i in range(k, n, 1):
    edge = scores[cnt]
    new_edge = scores[i]
    if edge < new_edge:
        print('Yes')
    else:
        print('No')
    cnt += 1
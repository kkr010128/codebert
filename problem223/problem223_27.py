N, K = map(int, input().split())
expectation = list(map(lambda x: (x+1) / 2, map(int, input().split())))
cur_expectation = sum(expectation[:K])
max_expectation = cur_expectation
for i in range(N - K):
    cur_expectation -= expectation[i]
    cur_expectation += expectation[i + K]
    if cur_expectation > max_expectation:
        max_expectation = cur_expectation
print(max_expectation)

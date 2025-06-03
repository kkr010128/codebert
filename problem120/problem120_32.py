N, K = list(map(int, input().split()))

price_list = list(map(int, input().split()))

price_list.sort()

answer = 0

for i in range(K):
    answer += price_list[i]

print(answer)
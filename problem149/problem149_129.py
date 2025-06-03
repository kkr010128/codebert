N, M, X = map(int, input().split())
book_lists = [list(map(int, input().split())) for _ in range(N)]
max_cost = 10**5*12+1
min_cost = max_cost

for i in range(1, 2**N):
   score_list = [0 for _ in range(M)]
   cost = 0
   for j in range(N):
       if i >> j & 1:
           cost += book_lists[j][0]
           for k in range(M):
               score_list[k] += book_lists[j][k+1]
   if min(score_list) >= X:
       min_cost = min(cost, min_cost)

print(min_cost if not min_cost == max_cost else -1)


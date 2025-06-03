N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
sum_now = 0
cost = 99999999999
for a in A:
  sum_now += a
  cost = min(cost, abs(sum_now - (sum_A - sum_now)))
print(cost)

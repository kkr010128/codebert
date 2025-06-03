N, K = map(int, input().split())
lst = [0 for _ in range(N)]
for i in range(K):
  d = int(input())
  A = list(map(int, input().split()))
  for j in range(d):
    lst[A[j] - 1] += 1
print(lst.count(0))
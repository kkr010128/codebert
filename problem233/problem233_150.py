N = int(input())
P = list(map(int,input().split()))
n = float("INF")
count = 0
for i in P:
  if n >= i:
    n = i
    count += 1
print(count)
N = int(input())
P = list(map(lambda p : int(p), input().split(" ")))
left_min = P[0]
cnt = 0
for i in range(len(P)):
  if left_min >= P[i]:
    cnt += 1
    left_min = P[i]
print(cnt)
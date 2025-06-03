N = int(input())
X = [int(x) for x in list(input().split())]
max_x = max(X)
min_x = min(X)
d = max_x - min_x
middle = (d//2)
P = middle + min_x
ans = 0
for i in range(N):
  ans += (max_x-X[i])**2
for i in range(d):
  n_ans = 0
  P = min_x + i
  for j in range(N):
    n_ans += (P-X[j])**2
  if (n_ans < ans):
    ans = n_ans
print(int(ans))
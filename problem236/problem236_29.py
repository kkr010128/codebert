H = int(input())
W = int(input())
N = int(input())

ans = 0
num = 0
big = 0
if H < W:
  big = W
else:
  big = H
while num < N:
  num += big
  ans += 1
  
print(ans)
from bisect import bisect_right

N, D, A = map(int, input().split())
xh = sorted([list(map(int, input().split())) for _ in range(N)])
ds = [0]*(N+2)
b = 0
for i, (x, h) in enumerate(xh, 1):
  ds[i] += ds[i-1]###(*)
  ###これまでのやつに与えたダメージは引き継がれるものとする
  d = ds[i]
  if d>=h:
    continue###すでに体力以上のダメージを与えた敵
  h -= d###ダメージを与える
  times = h//A if h%A==0 else h//A+1
  ds[i] += times*A
  ds[bisect_right(xh, [x+2*D, float('inf')])+1] -= times*A
  ###(*)のせいで, 2Dよりも向こう側にも、今考えたダメージの影響が
  ###出てしまうので. それを打ち消すために与えるダメージを引いておく
  b += times
print(b)

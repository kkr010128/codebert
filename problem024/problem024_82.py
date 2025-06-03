import math

p_max = 1000000 * 1000000
n, k = map(int, input().split())
w = [int(input()) for i in range(n)]

def check(p):
  i = 0
  for j in range(k):
    s = 0
    while (s + w[i] <= p):
      s += w[i]
      i += 1
      if i == n:
        return n
  return i

if __name__ == "__main__":
  right = p_max
  left = 0
  mid = 0
  while (right - left > 1):
    mid = math.floor((right + left) / 2)
    v = check(mid)
    if v >= n:
      right = mid
    else:
      left = mid
  
  print (right)

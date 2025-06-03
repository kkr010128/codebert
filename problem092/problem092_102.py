# -*- using:utf-8 -*-

class main:
  def function(x, k, d):
    if x >= k * d:
      ans = x - k * d
    else:
      r = x // d
      n = k - r
      if n % 2 == 0:
        ans = x % d
      else:
        ans = abs(x % d - d)
    return ans

if __name__ == "__main__":
  x, k, d = map(int, input().split())
  x = abs(x)
  ans = main.function(x, k, d)
  print(ans)
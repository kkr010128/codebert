import math


def get_int_list():
  return list(map(int, input().split()))


n, x, t = get_int_list()
ans = math.ceil(n / x) * t
print(ans)
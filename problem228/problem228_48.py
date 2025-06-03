import math
h = int(input())
num = math.log(h,2)
num = int(num)
ans = 0
for i in range(num+1):
  ans += 2**i

print(ans)
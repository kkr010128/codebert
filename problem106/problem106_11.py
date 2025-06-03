n = int(input())
ans = [0] * 10010

def get_ans(n):
  cnt = 0
  for x in range(1, 101):
    for y in range(1, 101):
      for z in range(1, 101):
        k = x**2 + y**2 + z**2 + x*y + y*z + z*x
        if(k <= 10000):
          ans[k] += 1        
  return ans

ans = get_ans(n)
for i in range(1, n+1):
  print(ans[i])
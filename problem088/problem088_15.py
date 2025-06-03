n = int(input())
a = list(map(int, input().split()))

def judge(x, y):
  if x > y:
    return(x-y)
  else:
    return(0)
ans = 0
for i in range(n - 1):
  xy = judge(a[i], a[i+1])
  a[i+1] += xy
  ans += xy
  
print(ans)
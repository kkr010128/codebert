n = int(input())
l = list(map(int, input().split()))

def judge(l, i, j, k):
  a = l[i]
  b = l[j]
  c = l[k]
  if a != b and b != c and c != a:
    if a + b > c and b + c > a and c + a > b:
      return 1
    else:
      return 0
  else:
    return 0
cnt = 0
for i in range(n - 2):
  for j in range(i + 1, n - 1):
    for k in range(j + 1, n):
      cnt += judge(l, i, j, k)
      
print(cnt)
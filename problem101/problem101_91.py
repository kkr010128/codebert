a, b, c = map(int, input().split())
k = int(input())
p = "No"
for i in range(k):
  if not(a < b and b < c):
    if b <= a:
      b = b * 2
    else:
      c = c * 2
if a < b and b < c:
  p = "Yes"
print(p)
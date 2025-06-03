a, b =map(int, input().split())

m = a*b
lst = []
for i in range(1, b+1):
  if m < a*i:
    break
  lst.append(a*i)

for j in lst:
  if j%b == 0:
    print(j)
    break
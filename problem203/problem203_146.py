a = list(map(int,input().split()))
p = a[0]
q = a[1]
for i in range(2000):
  if int(i*0.08) == p and int(i*0.1) == q:
    print(i)
    break
  if i == 1999:
    print(-1)
n,d = map(int,input().split())
cnt = 0
md = d**2
for _ in range(n):
  a,b = map(int,input().split())
  if md >= (a**2+b**2):
    cnt += 1
print(cnt)

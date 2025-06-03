n,x,y = map(int,input().split())

x -= 1
y -= 1
cnt = [0]*n

for i in range(n):
  for j in range(i+1,n):
    dis = min(j-i,abs(x-i)+1+abs(j-y))
    cnt[dis] += 1
for i in range(1,n):
  print(cnt[i])
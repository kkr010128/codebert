ans = 0
N,d = [int(i) for i in input().split(" ")]
for i in range(N):
  x,y = [int(i) for i in input().split(" ")]
  if x**2 + y**2 <= d**2:
    ans +=1
print(ans)
N = int(input())
ans = 0
for i in range(1,int((N+1)/2)):
  if i != N - i:
    ans += 1
print(ans)

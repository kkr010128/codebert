H = int(input())
ans,attack = 1,0
while(H > 1):
  attack += 1
  H //= 2
for i in range(1,attack+1):
  ans += 2**i
print(ans)
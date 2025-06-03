k = int(input())
ans = 1
a = 7 % k

while a != 0:
  ans += 1
  a = (10*a + 7) % k
  
  if ans == 10**6:
    ans = -1
    break
print(ans)
n = int(input())
s = input()
ans = 0
 
#print(s.count('ABC'))
for ni in range(n):
  if s[ni:ni+3] == 'ABC':
    ans += 1
print(ans)
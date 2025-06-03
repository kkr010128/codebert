n = int(input())
s = list(input())

r = s.count('R')
g = s.count('G')
b = n - r - g
ans = r*g*b

for i in range(n-2):
  for j in range(i+1,i+((n-i-1)//2)+1):
    if s[i] != s[j] and s[i] != s[2*j - i] and s[j] != s[2*j - i]:
      ans -= 1
      
print(ans)
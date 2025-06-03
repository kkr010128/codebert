def solve(n,s):
  cnt = 0
  for i in range(len(s)-2):
    if "A" == s[i] and "B" == s[i+1] and "C" == s[i+2]:
      cnt+=1
  return cnt
 
n = int(input())
s = input()
ans = solve(n,s)
print(ans)
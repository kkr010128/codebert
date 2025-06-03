S = input()
N = len(S)
s = S[:(N-1)//2]
t = S[(N+3)//2-1:]
 
if s == t[::-1] and s == s[::-1] and t == t[::-1]:
  ans = "Yes"
else:
  ans = "No"
  
print(ans)
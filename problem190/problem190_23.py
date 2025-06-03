S = input()
 
N = len(S)
ans = 'No'
 
# 文字列strの反転は、str[::-1]
if S == S[::-1] and S[:(N-1)//2] == S[:(N-1)//2][::-1] and S[(N+1)//2:] == S[(N+1)//2:][::-1]:
  ans = 'Yes'
  
print(ans)
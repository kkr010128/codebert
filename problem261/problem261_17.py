S = str(input())
l = len(S)

if l % 2 == 0:
  A = S[:(l//2)]
  B = S[(l//2):]
else:
  A = S[:(l//2)]
  B = S[(l//2+1):]
  
B = B[::-1]
ans = 0
for i in range(l//2):
  if A[i] != B[i]:
    ans += 1
    
print(ans)
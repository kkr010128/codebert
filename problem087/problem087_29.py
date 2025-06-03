N=int(input())
S=str(N)
A=len(S)
M=0
for i in range(A):
  M=M+int(S[i])
if M%9==0:  
  print("Yes")
else:
  print("No")
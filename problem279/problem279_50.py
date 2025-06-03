N=int(input())
S=list(input())
if N%2==1:
  print("No")
else:
  n=int(N/2)
  if S[0:n]==S[n:N]:
    print("Yes")
  else:
    print("No")

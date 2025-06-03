N,M=map(int, input().split())
if N in [0,1]:n=0
else:
  n=N*(N-1)/2
if M in [0,1]:m=0
else:
  m=M*(M-1)/2
print(int(n+m))
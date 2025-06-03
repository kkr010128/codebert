S=0
a,b=map(int,input().split())
for N in range(b,a+2):
  S+=(((a-N+1)*N)+1)
print(S%(10**9+7))
N = int(input())
S,T = input().split()
for s,t in zip(S,T):
  print(s+t,end="")
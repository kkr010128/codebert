for s in iter(input,'-'):
 for _ in range(int(input())):
  n=int(input())
  s=s[n:]+s[:n]
 print(s)

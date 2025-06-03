k=int(input())
n=input()
x=len(n)
if(x>k):
  print(n[0:k]+"...")
else:
  print(n)
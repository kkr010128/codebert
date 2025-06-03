H=int(input())
def f(H):
  if H==1:
    return 1
  elif H>1:
    return 2*f(H//2)+1
re=0
re=f(H)
print(re)
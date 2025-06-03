import sys
sys.setrecursionlimit(10**7)

H = int(input())

def f(h):
  if h == 1:
    return 1
  else:
    return 1 + f(h//2)*2
  
print(f(H))
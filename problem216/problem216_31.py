import math

def main():
  A, B, C = map(int, input().split())
  
  if A == B and B != C:
    print('Yes')
  elif A == C and A != B:
    print('Yes')
  elif B == C and B != A:
    print('Yes')
  else:
    print('No')
  
  
main()
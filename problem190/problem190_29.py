S=input()
N=len(S)
def isKaibun(S):
  #print(S,S[::-1])
  if S==S[::-1]:
    return True
  return False
if isKaibun(S) and isKaibun(S[:(N-1)//2]) and isKaibun(S[(N+3)//2-1:]):
  print("Yes")
else:
  print("No")
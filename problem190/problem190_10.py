S = input()

def kaibun(S):
  for i in range(len(S) // 2):
    if S[i] != S[len(S) - i - 1]:
      return False
  return True

if kaibun(S) and kaibun(S[:(len(S) - 1)//2]) and kaibun(S[(len(S) + 3) // 2-1:]):
  print('Yes')
else:
  print('No')
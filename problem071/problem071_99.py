S = input()

n = len(S)

S_a = list(S)

if S[n-1] == 's' :
  print(S + 'es')
  
else :
  print(S + 's')


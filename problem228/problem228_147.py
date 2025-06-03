H=int(input())

def n_attack(h):
  if h==1:return(1)
  else:return 1+2*n_attack(h//2)

print(n_attack(H))
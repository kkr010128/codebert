N, P = map(int, input().split())
S = input()
total = 0
if P == 2:
  for idx, right_value in enumerate(S, 1):
    if int(int(right_value)%2==0):
      total += idx
elif P == 5:
  valid_options = (0, 5)
  for idx, right_value in enumerate(S, 1):
    if int(int(right_value) in valid_options):
      total += idx
else:
  histo_modsuffix = [0]*P
  previous = 0
  for i, val in enumerate(reversed(S)):
    scale = pow(10, i, P)
    new_val = (previous + scale*int(val))%P
    histo_modsuffix[new_val] += 1
    previous = new_val
  for val in histo_modsuffix:
    total += val*(val-1)//2
  total += histo_modsuffix[0] # when right hand side is at far end
print(total)
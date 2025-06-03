S = input()
l = len(S) // 2
ll = l // 2
former = S[:l]
latter = S[l+1:]

for i in range(l):
  if S[i] != S[-i-1]:
    print("No")
    break
else:
  for i in range(ll):
    if former[i] != former[-i-1] or latter[i] != latter[-i-1]:
      print("No")
      break
  else:
    print("Yes")
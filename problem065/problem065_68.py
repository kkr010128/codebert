W = input().lower()
T = ""
while True:
  inp = input().strip()
  if inp == 'END_OF_TEXT':
    break
  T += inp.strip().lower()+' '


print(T.split().count(W))
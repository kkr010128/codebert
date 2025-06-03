s = input()
if len(s) %2 !=0:
  print("No")
else:
  c =0
  for i in range(len(s)//2):
    hi = s[2*i:2*i+2]
    if hi == "hi":
      pass
    else:
      c = 1
      break
  if c ==0:
    print("Yes")
    
  else:
    print("No")

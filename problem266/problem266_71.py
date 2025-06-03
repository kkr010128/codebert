x = int(input())
ans = 0
flag = False
for a in range((x//100)+1):
  for b in range((x//101)+1):
    for c in range((x//102)+1):
      for d in range((x//103)+1):
        for e in range((x//104)+1):
          for f in range((x//105)+1):           
            if (100*a) + (101*b) + (102*c) + (103*d) + (104*e) + (105*f)== x:
              ans += 1
              flag = True
              break
          if flag:
            break
        if flag:
          break
      if flag:
        break
    if flag:
      break
  if flag:
    break
  
if ans == 0:
  print(0)
else:
  print(1)

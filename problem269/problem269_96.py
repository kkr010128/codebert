T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

len1 = T1 * A1 + T2 * A2
len2 = T1 * B1 + T2 * B2
if len1 == len2:
  print("infinity")
  quit()

ans = 0
subs = 0  
sub1 = T1 * (A1 - B1)
sub2 = T2 * (A2 - B2)

if sub1 > 0:
  if len1 - len2 > 0:
    ans = 0
  else:
    S = (-1 * sub1) // (sub1 + sub2)
    T = (-1 * sub1) % (sub1 + sub2)
    if T == 0:
      ans = 2 * S
    else:
      ans = 2 * S + 1
else:
  if len1 - len2 < 0:
    ans = 0
  else:
    S = (-1 * sub1) // (sub1 + sub2)
    T = (-1 * sub1) % (sub1 + sub2)
    if T == 0:
      ans = 2 * S
    else:
      ans = 2 * S + 1
    
print(ans) 
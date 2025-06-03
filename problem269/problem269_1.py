T1, T2 = map(int,input().split())
A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())

T = T1*A1+T2*A2
A = T1*B1+T2*B2
if T == A:
  print("infinity")
  exit()

if T > A:
  if A1 > B1:
    print(0)
    exit()
  else:
    tdif = T-A #7-5
    pdif = T1*(B1-A1) #5
    if pdif%tdif == 0:
      ans = 2*(pdif//tdif)+1
    else:
      ans = 2*(1+pdif//tdif)
    ans -=1 #原点の分を引く
else:
  if B1 > A1:
    print(0)
    exit()
  else:
    tdif = A-T #7-5
    pdif = T1*(A1-B1) #5
    if pdif%tdif == 0:
      ans = 2*(pdif//tdif)+1
    else:
      ans = 2*(1+pdif//tdif)
    ans -=1 #原点の分を引く    
print(ans)
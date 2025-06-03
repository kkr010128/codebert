while 1:
  H, W=map(int, raw_input().split())
  if H==0 and W==0:
    break
  for i in range(H):
    L=list("#"*W)
    if i==0 or i==(H-1):
      s="".join(L)
      print s
    else:
      for j in range(1, W-1):
        L[j]="."
        s="".join(L)
      print s
  print ""
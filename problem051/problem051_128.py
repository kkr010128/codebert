while 1:
  H, W=map(int, raw_input().split())
  if H==0 and W==0:
    break
  for i in range(H):
    L=list("#"*W)
    if i%2==0:
      for j in range(W):
        if j%2!=0:
          L[j]="."
      s="".join(L)
      print s
    else:
      for j in range(W):
        if j%2==0:
          L[j]="."
        s="".join(L)
      print s
  print ""
while True:
  H,W = map(int,input().split())
  if H == 0 and W == 0 :
    break
  line = ['#.'*(W // 2)+'#'*(W % 2),'.#'*(W // 2)+'.'*(W % 2)]
  for i in range(H) :
    print(line[i % 2])
  print()

while 1:
  h,w=map(int,raw_input().split())
  if h==0:exit()
  print'#'*w
  for i in range(h-2):print'#'+'.'*(w-2)+'#'
  print'#'*w
  print
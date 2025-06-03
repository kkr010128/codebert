while 1:
  h,w = map(int, raw_input().split())
  if h==w==0:
    break

  for i in range(0,h/2):
    print ("#." * (w/2) + "#" * (w%2))
    print (".#" * (w/2) + "." * (w%2))

  if h % 2 == 1:
    print ("#." * (w/2) + "#" * (w%2))

  print ""
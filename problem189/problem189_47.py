n, m = map(int, input().split())
if m >= 2:
  if n < 2:
    print(int(m*(m-1)/2))
    quit()
  else:
    print(int(m*(m-1)/2 + n*(n-1)/2))
    quit()
    
if m < 2:
  if n < 2:
    print(0)
  else:
    print(int(n*(n-1)/2))
  

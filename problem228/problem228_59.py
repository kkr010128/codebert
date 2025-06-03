def check(h):
  if h > 1:
    return 2*(check(h//2))+1
  elif h==1:
    return 1
print(check(int(input())))
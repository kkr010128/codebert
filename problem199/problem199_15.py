def solve():
  s = input()
  n = len(s)
  if n%2 == 1:
    print("No")
  else:
    tmp = "hi"*(n//2)
    if s == tmp:
      print("Yes")
    else:
      print("No")
solve()
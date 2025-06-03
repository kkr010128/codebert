s = input()
for _ in range(int(input())):
  c = input().split()
  a = int(c[1])
  b = int(c[2])
  if c[0] == "replace":
    s = s[:a] + c[3] + s[b+1:]
  elif c[0] == "reverse":
    s = s[:a] + s[a:b+1][::-1] + s[b+1:]
  else:
    print(s[a:b+1])

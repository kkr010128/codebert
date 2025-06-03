s = input()
q = int(input())
#+---+---+---+---+---+---+
#| P | y | t | h | o | n |
#+---+---+---+---+---+---+
#0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1
for i in range(0, q):
  l = list(input().split())
  a = int(l[1])
  b = int(l[2]) + 1
  if l[0] == "print":
    print(s[a: b])
  elif l[0] == "reverse":
    rev = s[a: b]
    rev = rev[::-1]
    s = s[:a] + rev + s[b:]
  else:
    s = s[:a] + l[3] + s[b:]


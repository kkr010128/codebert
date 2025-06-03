s = list(input())
t = list(input())
if s == t:
  print(0)
else:
    changes = 0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            changes += 1
    print(changes)
s = input()
t = input()

ans = 10 ** 8
for i in range(len(s)-len(t)+1):
  check = 0
  for j in range(len(t)):
    if s[i+j] != t[j]:
      check = check + 1
  if ans > check:
    ans = check
print(ans)
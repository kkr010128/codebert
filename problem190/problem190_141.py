def flg(s):
  le = len(s) // 2
  return s[:le] == s[::-1][:le]


s = input()
le1 = len(s) // 2
t = s[:le1]

print(["No", "Yes"][flg(s) and flg(t)])
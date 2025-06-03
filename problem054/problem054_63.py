n = int(input())
s_l = []
h_l = []
c_l = []
d_l = []
for i in range(1, 14):
  s_l.append(i)
  h_l.append(i)
  c_l.append(i)
  d_l.append(i)

for i in range(0, n):
  mark, num = input().split()
  if mark == "S":
    s_l.remove(int(num))
  if mark == "H":
    h_l.remove(int(num))
  if mark == "C":
    c_l.remove(int(num))
  if mark == "D":
    d_l.remove(int(num))

for s in s_l:
  print("S {}".format(s))
for h in h_l:
  print("H {}".format(h))
for c in c_l:
  print("C {}".format(c))
for d in d_l:
  print("D {}".format(d))
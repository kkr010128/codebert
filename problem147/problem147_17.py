s = input()
t = input()

t_2 = []
for i in range(len(t) - 1):
  t_2.append(t[i])
  
line = "".join(t_2)
if line == s:
  print("Yes")
else:
  print("No")
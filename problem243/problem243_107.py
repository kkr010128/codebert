n = int(input())
st = []
for _ in range(n):
  si, ti = input().split()
  st.append((si, int(ti)))
name = input()
count = 0
flag = False
for i in range(n):
  if flag:
    count += st[i][1]
  if st[i][0] == name:
    flag = True
print(count)
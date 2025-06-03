st = set()
n = int(input())
ls = [int(x) for x in input().split()]
for i in ls:
  st.add(i)
  
if len(st) == n:
  print("YES")
else:
  print("NO")
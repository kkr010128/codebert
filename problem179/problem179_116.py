n,m = map(int,input().split())
a = list(map(int,input().split()))
m_count = 0
a_sum = sum(a)
for i in a:
  if i >= (a_sum/(4*m)):
    m_count += 1
  else:
    continue
    
if m_count >= m:
  print("Yes")
else:
  print("No")
x = 0
m_list = []
f_list = []
r_list = []
while x < 50:
  m, f, r = map(int, input().split())
  if m == -1 and f == -1 and r == -1:
    break
  m_list.append(m)
  f_list.append(f)
  r_list.append(r)
  x = x+1
  
for(mlist,flist,rlist) in zip(m_list,f_list,r_list):
  if mlist == -1 or flist == -1:
    print("F")
  elif 80 <= mlist + flist:
    print("A")
  elif 65 <= mlist + flist and mlist + flist < 80:
    print("B")
  elif 50 <= mlist + flist and mlist + flist < 65:
    print("C")
  elif 30 <= mlist + flist and mlist + flist < 50:
    if 50 <= rlist:
      print("C")
    else:
      print("D")
  elif mlist + flist < 30:
    print("F")

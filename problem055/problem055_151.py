n=input()
L1=[[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0]]
L2=[[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0]]   
L3=[[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0]]
L4=[[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0]]
Mantion=[L1,L2,L3,L4]
for i in range(n):
  b,f,r,v=map(int, raw_input().split())
  Mantion[b-1][f-1][r-1]+=v

for j in range(3):
  L1_str=map(str, L1[j])
  print "",
  print " ".join(L1_str)
print "#"*20
for j in range(3):
  L2_str=map(str, L2[j])
  print "",
  print " ".join(L2_str)
print "#"*20
for j in range(3):
  L3_str=map(str, L3[j])
  print "",
  print " ".join(L3_str)
print "#"*20
for j in range(3):
  L4_str=map(str, L4[j])
  print "",
  print " ".join(L4_str)
from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import Counter

h,w,m=nii()

h_bomb=[0 for i in range(h)]
w_bomb=[0 for i in range(w)]

l=set()
for i in range(m):
  th,tw=nii()
  th-=1
  tw-=1
  h_bomb[th]+=1
  w_bomb[tw]+=1
  l.add((th,tw))

h_max=max(h_bomb)
w_max=max(w_bomb)

h_cand=[]
w_cand=[]

for i in range(len(h_bomb)):
  if h_bomb[i]==h_max:
    h_cand.append(i)

for i in range(len(w_bomb)):
  if w_bomb[i]==w_max:
    w_cand.append(i)

for i in h_cand:
  for j in w_cand:
    if (i,j) not in l:
      print(h_max+w_max)
      exit()

print(h_max+w_max-1)

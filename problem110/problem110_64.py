from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

h,w,k=nii()
c=[list(input()) for i in range(h)]

b_cnt=0
for i in c:
  b_cnt+=i.count('#')

ans=0
for i in range(2**h):
  for j in range(2**w):
    h_use=[]
    for ii in range(h):
      if (i>>ii)&1:
        h_use.append(ii)
    w_use=[]
    for jj in range(w):
      if (j>>jj)&1:
        w_use.append(jj)

    t_cnt=0
    for s in h_use:
      t_cnt+=c[s].count('#')
    for s in w_use:
      for t in range(h):
        if c[t][s]=='#':
          t_cnt+=1

    for s in h_use:
      for t in w_use:
        if c[s][t]=='#':
          t_cnt-=1

    if b_cnt-t_cnt==k:
      ans+=1

print(ans)
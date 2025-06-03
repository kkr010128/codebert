import copy
h,w,k=map(int,input().split())
M=[list(input()) for _ in range(h)]
a=0
for i in range(2**w):
  for j in range(2**h):
    b=0
    for c in range(w):
      for r in range(h):
        if (i>>c)&1==0 and (j>>r)&1==0 and M[r][c]=='#':
          b+=1
    if b==k:
      a+=1
print(a)    
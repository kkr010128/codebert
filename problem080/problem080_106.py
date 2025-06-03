from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())

z=[]
w=[]
for i in range(n):
  x,y=nii()
  z.append(x-y)
  w.append(x+y)

z_ans=max(z)-min(z)
w_ans=max(w)-min(w)
print(max(z_ans,w_ans))
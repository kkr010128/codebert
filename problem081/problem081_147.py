from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

d,t,s=nii()
print('Yes' if d/s<=t else 'No')
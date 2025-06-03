from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b,c=nii()

print('Yes' if c-a-b>=4 and 4*a*b<(c-a-b)**2 else 'No')
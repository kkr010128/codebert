from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

h1,m1,h2,m2,k=nii()
minute=(h2-h1)*60
minute+=m2-m1
minute-=k

print(minute)
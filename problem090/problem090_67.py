S = input()[0:3]

i=S.count('RRR')
j=S.count('RR')
k=S.count('R')
l=S.count('RSR')

print(max(i,j,k-l))
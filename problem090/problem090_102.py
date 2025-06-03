s=input()
l=[['SSS'],['RSS','SRS','SSR','RSR'],['RRS','SRR'],['RRR']]
for i in range(4):
  if s in l[i]:
    print(i)
    exit()
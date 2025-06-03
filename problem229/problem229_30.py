(h,n),*t=[map(int,o.split())for o in open(0)]
d=[0]+[9e9]*h
for a,b in t:
 for j in range(h+1):d[j]=min(d[j],d[max(0,j-a)]+b)
print(d[h])
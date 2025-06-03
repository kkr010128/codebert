(h,n),*t=[list(map(int,o.split()))for o in open(0)]
d=[0]*10**8
for i in range(h):d[i+1]=min(b+d[i-a+1]for a,b in t)
print(d[h])
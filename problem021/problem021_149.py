l={}
s=[]
h=[0]
n=d=m=0
for c in raw_input():
    if c=="\\":
        l[d]=n
        d-=1
    elif c=="/":
        d+=1
        if d in l:
            while len(s) and s[-1][1]>l[d]: s.pop()
            s.append([l[d],n])
    n+=1
    h.append(d)

a=[sum([h[i]-k for k in h[i:j+1]]) for i,j in s]
print sum(a)
print " ".join(map(str,[len(a)]+a))
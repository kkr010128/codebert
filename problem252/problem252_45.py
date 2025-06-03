import numpy as np

n,m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
d = 2**18

f = np.array([0]*d)
for i in a:
    f[i]+=1

tf = np.fft.fft(f)
f = np.fft.ifft(tf*tf)
f = [int(i+0.5) for i in f]

ans=0
for i in range(len(f)-1,0,-1):
    if f[i]<=m:
        ans+=i*f[i]
        m-=f[i]
    elif f[i]>m:
        ans+=i*m
        break
print(ans)
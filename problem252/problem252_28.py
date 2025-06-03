import sys
input=sys.stdin.readline
import numpy as np
from numpy.fft import rfft,irfft

n,m=[int(j) for j in input().split()]
l=np.array([int(j) for j in input().split()])

a=np.bincount(l)

fft_len=1<<18
fft = np.fft.rfft
ifft = np.fft.irfft
Ff = fft(a,fft_len)
x=np.rint(ifft(Ff * Ff,fft_len)).astype(np.int64)
p=x.cumsum()
i=np.searchsorted(p,n*n-m)

q=n*n-m-p[i-1]

ans=(x[:i]*np.arange(i,dtype=np.int64)).sum()+i*q

print(int(l.sum()*2*n-ans))



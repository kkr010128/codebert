from numpy import*
n,m,*a=int_(open(0).read().split())
a=int_(fft.irfft(fft.rfft(bincount(a,[1]*n,2**18))**2)+.5)
c=0
for i in where(a>0)[0][::-1]:t=min(m,a[i]);c+=i*t;m-=t
print(c)
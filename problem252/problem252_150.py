import numpy as np

N,M = map(int,input().split())
A = list(map(int,input().split()))
Amax=max(A)

n0 = 2**int(np.ceil(np.log2(2*Amax+1)))#Amax+1以上となる最小の2のべき乗数

Afre=np.zeros(n0).astype(int)#パワーの頻度(1~Amax+1)
for i in range(N):
    Afre[A[i]]+=1

#astype(int)は切り捨てなので，rintで四捨五入してから．
S = np.rint(np.fft.irfft(np.fft.rfft(Afre)*np.fft.rfft(Afre))).astype(int)
Scum =S.cumsum()#累積和
bd = N*N-M#上からM個を取り出したい
i=np.searchsorted(Scum,bd)#価値iを生み出せる組みがM個以上ある
#価値iが生み出せる選び方の余分なものを引きたい
remove=((Scum[-1]-Scum[i])-M)*i
ans=0
for j in range(i+1,n0):
    ans+=S[j]*j
print(ans-remove)
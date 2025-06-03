N = int(input())
A = list(map(int,input().split()))
#t:  1, 2, 3,..., N
#A: A1,A2,A3,...,AN
#|t-s| = At+As となるt,sのペアの数は、
# t-s  = At+As かつ t>s となるt,sのペアの数と等しく、
# t-At =  s+As かつ t>s となるt,sのペアの数と等しい
ms = [0]*N
ps = [0]*N
for i in range(N):
    ms[i],ps[i] = (i+1)-A[i],(i+1)+A[i]

msc,psc = {},{}
mi,pi = 0,0
out = 0
while mi<N:
    msc[ms[mi]] = msc.get(ms[mi],0)+1
    out += psc.get(ms[mi],0)
    psc[ps[mi]] = psc.get(ps[pi],0)+1
    mi+=1
    pi+=1
print(out)
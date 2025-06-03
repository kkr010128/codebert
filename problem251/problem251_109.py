import sys,math,collections,itertools
input = sys.stdin.readline

N,K=list(map(int,input().split()))
R,S,P=list(map(int,input().split()))
T = input().rstrip()
s =T.replace('r','P') #P
ss=s.replace('s','R') #R
sss=ss.replace('p','S') #S
sl = list(sss)

for i in range(K,N):
    if sl[i]==sl[i-K]:
        sl[i] = '0'

sc = collections.Counter(sl)

print(sc['R']*R + sc['P']*P + sc['S']*S)

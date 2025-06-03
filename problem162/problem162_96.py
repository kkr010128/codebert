import math
import fractions
import collections
import itertools
import pprint
N,M=map(int,input().split())

#rotateすれば他の部屋で同じ組み合わせが出てしまう<=>他の部屋の2数の数字の差が同じになってしまう
#前半分を偶数差、後ろ半分を奇数差と言った感じで上から詰めれば良い
#部屋数をMとして、1,2,...,Mの差を考える
l=[]
maemin=1
usiromax=N
for i in range(M,0,-1):
    if i%2==0:
        l.append([maemin,maemin+i])
        maemin=maemin+1
    else:
        l.append([usiromax-i,usiromax])
        usiromax=usiromax-1
#print(l)

for i in range(M):
    print(*l[i],sep=" ")




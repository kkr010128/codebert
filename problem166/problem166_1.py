import math
import fractions
import collections
import itertools
from collections import deque
S=input()
N=len(S)
cnt=0
l=[]
"""
cnt=0
p=10**9+7
for i in range(K,N+2):
    cnt=(cnt+((N-i+1)*i)+1)%p
    #print(((N-i+1)*i)+1)
print(cnt)
"""
amari=[0]*(N+1)
num=0
for i in range(N):
    num=num+pow(10,i,2019)*int(S[N-1-i])
    amari[i+1]=num%2019
#print(amari)
c=collections.Counter(amari)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
#for i in range(len(key)):
#    l.append([key[i],values[i]])#lは[要素i,n_i]の情報を詰めたmatrix
#xprint(l)
for i in range(len(values)):
    cnt=cnt+(values[i]*(values[i]-1))//2
print(cnt)
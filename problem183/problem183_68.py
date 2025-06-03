# -*- coding: utf-8 -*-
N=input()

#約数列挙
def make_divisors(n):
    divisors=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n/i:
                divisors.append(n/i)
    return divisors

#整数N-1の約数は全て答えにカウントして良い
ans=set(make_divisors(N-1))
wrong_ans=set(make_divisors(N-1))

K=make_divisors(N)  #Nの約数の集合
#整数Nの約数について条件にマッチングするかを1つ1つ調べる
for k in K:
    if k==1: continue
    n=N
    while n%k==0:
        n/=k
    else:
        if n==1 or n%k==1:
            ans.add(k)
print len(ans)-1

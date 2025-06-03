import math
import sys
from functools import lru_cache
sys.setrecursionlimit(10000000)

N = int(input())
A_list = [int(e) for e in input().split()]

#pairwise coprime …… 素因数分解したとき、共通のものが1個もない
#setwise coprime　…… 素因数分解したとき、全てで共通のものがない

#試し割の結果の辞書を求める
def make_trial_division_dict(n):
    #import math
    td_dict = dict()
    for i in range(2,n+1):
        if i not in td_dict:
            td_dict[i] = i
            for j in range(2,1+n//i):
                if j*i not in td_dict:
                    td_dict[j*i] = i
    td_dict[1] = 1
    return td_dict

#試し割結果の辞書を利用して素因数分解する
@lru_cache(maxsize=None)
def high_speed_prime_factorization(n):
    pf_list = list()
    pf_list.append(td_dict[n])
    
    if n//td_dict[n] == 1:
        if n!=1:
            pf_list.append(1)
        return pf_list
    else:
        pf_list.extend(high_speed_prime_factorization(n//td_dict[n]))
        return pf_list

td_dict = make_trial_division_dict(max(A_list))

all_pf = set()    #含まれる素因数がすべて集約される
common_pf = set() #共通する素因数が集約される
all_pf |= set(high_speed_prime_factorization(A_list[0]))
common_pf |= set(high_speed_prime_factorization(A_list[0]))
is_pairwise = True

#print(A_list[0],set(high_speed_prime_factorization(A_list[0])))

for i in range(1,len(A_list)):
    A_pf = set(high_speed_prime_factorization(A_list[i]))
    common_pf &= A_pf 
    
    #print(A_list[i],set(high_speed_prime_factorization(A_list[i])))
    
    if is_pairwise and len(all_pf&A_pf)!=1: #1は共通で含まれる
        is_pairwise = False
    else:
        all_pf |= A_pf

if is_pairwise:
    print("pairwise coprime")
elif len(common_pf) == 1: #1は共通で含まれる
    print("setwise coprime")
else:
    print("not coprime")

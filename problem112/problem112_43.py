import numpy as np
import sys
n,k = map(int,input().split())
a_list = sorted(map(int,input().split()))
mod = 10**9+7
if n-k < a_list.count(0):
    print(0)
    exit()
if (sum([1 for a in a_list if np.sign(a)!=-1])==0 and k%2==1) or (k==n and len([1 for a in a_list if np.sign(a)==-1])%2==1):
    a_list.sort(key = abs)
    ans = 1
    for num in a_list[:k]:
        ans *= num
        ans %= mod
    print(ans)
    exit()
else:
    a_list.sort(key = abs,reverse = True)
    add = 1
    remove = 1
    if len([a for a in a_list[:k] if np.sign(a)==-1])%2!=0:
        negative_big = [num for num in a_list[:k] if np.sign(num)==-1]
        positive_big = [num for num in a_list[:k] if np.sign(num)!=-1]
        negative_small = [num for num in a_list[k:] if np.sign(num)==-1]
        positive_small = [num for num in a_list[k:] if np.sign(num)!=-1]
        
        
        if len(negative_big)==0 or len(positive_small)==0:
            remove = min(positive_big)
            add = min(negative_small)
        elif len(positive_big)==0 or len(negative_small)==0:
            remove = max(negative_big)
            add = max(positive_small)
        else:
            positive_small_max = max(positive_small)
            negative_big_max = max(negative_big)
            negative_small_min = min(negative_small)
            positive_big_min = min(positive_big)
            if positive_small_max*positive_big_min > negative_small_min*negative_big_max:
                remove = negative_big_max
                add = positive_small_max
            else:
                remove = positive_big_min
                add = negative_small_min
ans = 1
for num in a_list[:k]:
    ans *= num
    ans %= mod
    
if len([a for a in a_list[:k] if np.sign(a)==-1])%2!=0:
    ans *= add
    ans %= mod
    ans *= pow(remove, mod-2, mod)
    ans %= mod

print(ans)
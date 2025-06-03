"""
import numpy as np
from collections import Counter

n = map(int,input().split())
a = list(map(int,input().split()))
Q = int(input())
a_count = dict(Counter(a))



def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)


#change_dict_key(a_count, 1, 5)

#print(a_count)



for q in range(Q):
    num = list(map(int,input().split()))
    
    if(num[0] not in a_count):
        print(np.dot( np.array(list(a_count.keys())) , np.array(list(a_count.values()) ) ) )
        continue

    if(num[1] not in a_count):
        change_dict_key(a_count,num[0],num[1])

    else :
        a_count[num[1]] += a_count[num[0]] 
        del a_count[num[0]] 
    
    #print(a_count.values())

    print(np.dot( np.array(list(a_count.keys())) , np.array(list(a_count.values()) ) ) )
    #print((sum(list_a))  )
"""
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

B, C = [0]*Q, [0]*Q
for i in range(Q):
    B[i], C[i] = list(map(int, input().split()))

bucket = [0]*100001
for i in A:
    bucket[i] += 1

sum = sum(A)

for i in range(Q):
    sum += (C[i] - B[i]) * bucket[B[i]]
    bucket[C[i]] += bucket[B[i]]
    bucket[B[i]] = 0
    print(sum)




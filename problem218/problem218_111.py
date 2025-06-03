# -*- coding: utf-8 -*-
import collections

N = int(input())

all_str = []
for i in range(N):
    str_temp = input()
    all_str.append(str_temp)
all_str.sort()
coll_str = (collections.Counter(all_str))
count_max = 0
j = 0
max_str = coll_str.most_common()
for i in max_str:
    
    num_of_str =  i[1]
    if num_of_str == count_max or j == 0:
        print(i[0])
        j = 1
        count_max = num_of_str
        
    if num_of_str < count_max:
        break

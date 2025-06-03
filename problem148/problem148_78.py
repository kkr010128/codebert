# -*- coding: utf-8 -*-
import sys

A,B,C,K = list(map(int, input().rstrip().split()))
#-----

sum_num = 0

for num,cnt in [(1,A), (0,B), (-1,C)]:
    if cnt <= K:
        K -= cnt
        sum_num += num*cnt
    else:
        print( sum_num + num*K )
        sys.exit()


print(sum_num)

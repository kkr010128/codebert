# -*- coding: utf-8 -*-
k,x = list(map(int,input().split()))

ret = "No"
if 500*k>=x:
    ret = "Yes"
print(ret)
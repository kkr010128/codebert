#!/usr/bin/env python
#coding: UTF-8
while True:
    h,w = map(int,raw_input().split())
    if h+w==0:
    	break
    else:
    	print w*'#'# ??????####
    	for hight in range(h-2):
            print '#'+(w-2)*'.'+'#'
        print w*'#'#????????????####
        print
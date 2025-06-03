# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 02:42:25 2020

@author: liang
"""

"""
n進数問題
【原則】　大きな数の計算をしない
　⇒　１の桁から計算する
 
171-C いびつなn進数

27 -> a(26)a(1)となる
　⇒先にa(1)だけもらってN%26とすることで解決
 
ASCII化 ord()
文字化　chr()
"""

N = int(input())

res = str()

while N > 0:
    N -= 1 #"a"として予め設置
    res += chr(ord("a") + N%26)
    N //= 26

print(res[::-1])
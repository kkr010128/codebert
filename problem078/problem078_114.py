#!/usr/bin python3
# -*- coding: utf-8 -*-

mod = 10**9+7
n = int(input())
ret = 0
ret += pow(10,n,mod)
ret -= 2 * pow(9,n,mod)
ret %= mod
ret += pow(8,n,mod)
ret %= mod
print(ret)

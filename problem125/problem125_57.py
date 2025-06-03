#!/usr/bin python3
# -*- coding: utf-8 -*-

from math import gcd        #for python3.8

def lcm(a,b):
    G = gcd(a, b) #最大公約数
    L = (a//G)*b #最小公倍数
    return L

def main():
    X = int(input())
    print(lcm(X,360)//X)

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

while True:
    n = int(raw_input())
    if n == 0:
        break
    else:
        sum = 0
        while n > 0:
            sum += n%10
            n /= 10
        print sum
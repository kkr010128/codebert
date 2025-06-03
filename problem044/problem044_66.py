#!/usr/bin/env python
# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())
ret = [i for i in range(a, b+1) if c%i == 0]
print(len(ret))
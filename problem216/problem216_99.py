#!/usr/bin/env python3
a = list(map(int, input().split()))
if len(a) - len(set(a)) == 1:
    print('Yes')
else:
    print('No')
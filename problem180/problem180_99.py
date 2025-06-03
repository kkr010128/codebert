# -*- coding: utf-8
a,b = map(int,input().split())
yon = 100000000000000000000000
a = a%b
yon = min(a,abs(a-b))
print(yon)
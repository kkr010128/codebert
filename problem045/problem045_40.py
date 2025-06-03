# -*- coding:utf-8 -*-

a,b = input().split()
a,b = int(a),int(b)

d = int(a//b)
r = int(a%b)

print(d,r,format(a/b,'.6f'))
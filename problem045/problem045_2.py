#coding:utf-8
'''
a ÷ b ： d (整数)
a ÷ b の余り ： r (整数)
a ÷ b ： f (浮動小数点数)
'''
a, b = map(int, input().split())
d = a // b
r = a % b
f = a / b
print('%d %d %.8f' % (d, r, f))



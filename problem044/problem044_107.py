#coding:utf-8

buff = [int(x) for x in input().split()]
a = buff[0]
b = buff[1]
c = buff[2]
print(len([x for x in [x+a for x in range(b - a + 1)] if c%x==0]))
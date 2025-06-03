#coding:utf-8
#1_1_D 2015.3.6
second = int(input())
hour = second // 3600
minutes = (second // 60) % 60
second %= 60
print("%s:%s:%s" %(hour,minutes,second))
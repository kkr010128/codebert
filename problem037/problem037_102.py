#coding:UTF-8

x = input()
a = x/3600
b = (x%3600)/60
c = (x%3600)%60
print str(a)+":"+str(b)+":"+str(c)
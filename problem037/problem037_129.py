a= int(input())
h = a//3600
m = (a%3600)//60
s = (a%3600)%60
print('%d:%d:%d' % (h, m, s))

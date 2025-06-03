x = input()
a = x/3600
b = x%3600/60
c = x - a*3600 - b*60
print '%d:%d:%d'%(a, b, c)
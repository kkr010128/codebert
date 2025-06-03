x = int(raw_input())
h = x / 3600
m = (x % 3600) / 60 
s = x % 60
print u"%d:%d:%d" %  (h,m,s)
a = int(raw_input())
 
b, c  = divmod(a, 3600)
d, e = divmod(c, 60)

print ("%d:%d:%d") % (b,d,e)
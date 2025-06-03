S = int(input())
h = int(S/3600)
left = S-3600*h
m = int(left/60)
s = left-60*m
print("{}:{}:{}".format(h,m,s)) 



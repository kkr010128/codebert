s=int(raw_input())
h=s/3600
m=(s-3600*h)/60
print "%d:%d:%d"%(h,m,s-3600*h-60*m)
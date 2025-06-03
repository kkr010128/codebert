s=input()

h=s/3600
m=s/60-h*60
s=s-h*3600-m*60

print str(h)+":"+str(m)+":"+str(s)


x=input()

l=(x/60)
h=(l/60)
m=(l-h*60)
s=x-m*60-h*60*60

print str(h)+":"+str(m)+":"+str(s)
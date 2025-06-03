S=input()
h=S/3600
r=S%3600/60
s=S-h*3600-r*60
print str(h)+':'+str(r)+':'+str(s)
a=[]
for i in range(4*13):a.append("SHCD"[i/13]+" "+str(i%13+1))
for i in range(input()):a.remove(raw_input())
for i in a:print i
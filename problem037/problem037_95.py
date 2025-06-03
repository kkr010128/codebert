S = int(input())
h = (S//(60*60))
m = ((S-3600*h)//60)
se = (S-3600*h-60*m)

print(str(h)+":"+str(m)+":"+str(se))

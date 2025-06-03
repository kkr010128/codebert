S=input()
n=int(S)
h=int(n/(60*60))
m=int((n-60*60*h)/60)
s=int(n-(60*60*h+60*m))
print(h,":",m,":",s, sep='')


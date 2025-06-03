l=raw_input()
k=l.split()
a=int(k[0])
b=int(k[1])
c=int(k[2])
#
ct=0
dev=a
while dev<=b:
        if c%dev==0:
                ct+=1
        dev+=1
print ct
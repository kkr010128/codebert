NXT= [int(i) for i in input().split(' ')]
i=NXT[0]
count=0
while i>0: 
    i -= NXT[1];count +=1
print(int(NXT[2]*count))
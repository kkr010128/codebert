X,Y=map(int,input().split())
count=0
if X==3:
  count = count+100000
elif X==2:
  count = count+200000
elif X==1:
  count = count+300000
else:
  count = count

if Y==3:
  count = count+100000
elif Y==2:
  count = count+200000
elif Y==1:
  count = count+300000
else:
  count = count
  
if X==1 and Y==1:
  count = count+400000
  
print(count)
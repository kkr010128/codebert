l=[0]*120
s="#"*20
for i in range(input()):b,f,r,v=map(int,raw_input().split());l[b*30+f*10+r-41]+=v
print "",
for i in range(120):
 print l[i],;j=i+1
 if j==120:break
 if j%30==0:print;print s,
 if j%10==0:print;print "",
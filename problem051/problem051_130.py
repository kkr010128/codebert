l='#.'*999
while 1:
 h,w=map(int,raw_input().split());s=""
 if h==0:break
 for i in range(h):s+=l[i%2:w+i%2]+"\n"
 print s
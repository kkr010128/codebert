while 1:
 m,f,r=map(int,input().split());s=m+f
 if r<0>s:break
 print('F'if m*f<0 or s<30 else'D'if(s<50)*(r<50)else'C'if s<65 else'B'if s<80 else'A')

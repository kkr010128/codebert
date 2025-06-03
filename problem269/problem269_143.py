T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())
OU=T1*(A1-B1)
HUKU=T2*(A2-B2)
TOTAL=OU+HUKU
if TOTAL==0:
 print("infinity")
elif (OU>0 and TOTAL>0) or (OU<0 and TOTAL<0):
 print(0)
elif (OU>0 and TOTAL*(-1)>OU) or (OU<0 and TOTAL*(-1)<OU):
 print(1)
else:
 K=int(OU/TOTAL)*-1
 if (OU%TOTAL)==0:
  print(K*2)
 else:
  print(K*2+1)

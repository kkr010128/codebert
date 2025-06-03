S=str(input())
 
if S.count('R')==0:
  print(0)
if S.count('R')==1 :
  print(1)
if S.count('R')==2 and not S.count('RR') ==1:
  print(1)
if S.count('RR')==1 and not S.count('RRR')==1:
  print(2)
if S.count('RRR')==1:
  print(3)
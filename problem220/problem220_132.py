list1=input().split()
S=list1[0]
T=list1[1]
A,B=map(int,input().split())
U=input()
if U==S:
  a=A-1
  print(f"{a} {B}")
if U==T:
  b=B-1
  print(f"{A} {b}")
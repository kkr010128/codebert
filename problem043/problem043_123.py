while True:
 a=map(int,raw_input().split())
 if a==[0,0]:
  break
 if a[0]>a[1]:print(str(a[1])+" "+str(a[0]))
 else: print(str(a[0])+" "+str(a[1]))
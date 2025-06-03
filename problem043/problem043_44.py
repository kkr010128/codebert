while True:
 a,b=map(int,input().split())
 if not(a) and not(b):break
 if a>b:a,b=b,a
 print(a,b)
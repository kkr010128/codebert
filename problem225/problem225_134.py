h,a = map(int,input().split())
ct=h//a

a=h-ct*a

if a>0:
  ct+=1
print(ct)
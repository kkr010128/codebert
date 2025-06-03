W=input()
s=0
while True:
 T=list(input().split())
 if T==['END_OF_TEXT']:
   break
 else:
   for i in T:
     if i.lower()==W.lower():
        s+=1
print(s)
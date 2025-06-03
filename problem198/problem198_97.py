N=int(input())
alpha=[chr(ord('a') + i) for i in range(26)]
l=[]
def ans(le,alp):
   s=len(set(alp))
   if le==N:
      l.append(alp)
      return
   for i in range(s+1):
      ans(le+1,alp+alpha[i])
ans(1,"a")
for i in l:
   print(i)
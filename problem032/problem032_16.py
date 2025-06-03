n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
list=[]
for j in range(3):
   D=0
   for i in range(n):
      if x[i]<y[i]:
         d = (y[i]-x[i])
      else:
         d = (x[i]-y[i])
      list.append(d)
      D += (d**(j+1))
   print(f"{D**(1/(j+1)):.6f}") 
print(f"{max(list):.6f}")


def lu(n):
  L.append(n)
  a=n%10
  if len(str(n))>11:
    return 1
  if a==0:
    lu(n*10+1)
    lu(n*10)
  elif a==9:
    lu(n*10+9)
    lu(n*10+8)
  else:
    lu(n*10+1+a)
    lu(n*10+a-1)
    lu(n*10+a)
L=list()
lu(1)
lu(2)
lu(3)
lu(4)
lu(5)
lu(6)
lu(7)
lu(8)
lu(9)
L=sorted(set(L))
k=int(input())
print(L[k-1])
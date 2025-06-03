n=int(input())
result=float('inf')
for i in range(1,int(n**.5)+1):
  if i*(n//i)==n:
    result=min(result,abs(i+n//i)-2)
print(result)
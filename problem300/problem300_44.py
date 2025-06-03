def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


a,b=map(int,input().split())

lst=make_divisors(a)
sin_lst=[]

for i in lst:
  if b%i==0:
    sin_lst.append(i)

if len(sin_lst)==1:
  print(1)
  exit()

lst=[]
lst.append(sin_lst[1])

for i in sin_lst[2:]:
  flag=True
  for j in lst:
    if i%j==0:
      flag=False
      break
  
  if  flag:
    lst.append(i)


print(len(lst)+1)
a, b, c = map(int, input().split())
i = a
j = 0
while(a <= i and i <= b) :
  if(c % i == 0) :
    i += 1
    j += 1
  else :
    i += 1
else :
  print(j)


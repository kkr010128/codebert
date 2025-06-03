x,k,d = map(int,input().split())

min_p = abs(x)//d
min_n = min_p + 1
rest_p = abs(x)- d*min_p
rest_n = rest_p - d

if k < min_p:
  print(abs(x) - k*d)
elif (k-min_p) % 2 == 0:
  print(rest_p)
else:
  print(abs(rest_n))
    


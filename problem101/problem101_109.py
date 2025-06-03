n , m , l = map(int , input().split())
k=int(input())
for a in range(k+1):
  for b in range(k+1):
    for c in range(k+1):
      a1 = (n*(2**a))
      b1 = (m*(2**b))
      c1 = (l*(2**c))
      if a+b+c <= k and a1 < b1 and b1 < c1:
        print("Yes")
        exit()
        
print('No')
N = int(input())

ans = [0 for i in range(10100)]

for x in range(1,100):
   for y in range(1,100):
      for z in range(1,100):
          n =  x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
          if n < 10100:
            ans[n] += 1

for n in range(N):
   print(ans[n+1])
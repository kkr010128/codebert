while True:
   n = int(input())
   if n == 0:
      break

   s = list(map(int, input().split()))
   
   m = sum(s) / n
   b = 0
   for i in range(n):
      b += (s[i] - m) ** 2
   
   ans = (b / n) ** 0.5
   print(ans)

   

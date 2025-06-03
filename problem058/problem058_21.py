ret = []
while True:
   n, x = map(int, raw_input().split())
   num_arr = [i for i in range(1, n+1)]
   if (n, x) == (0, 0):
       break

   cnt = 0
   for i in range(n, 0, -1):
       for j in range(i -1, 0, -1):
           if 0 < x - i - j < j:
               cnt += 1
          
   ret += [cnt]
for i in ret:
    print i
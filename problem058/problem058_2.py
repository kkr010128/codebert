ret = []
while True:
   n, x = map(int, raw_input().split())
   num_arr = [i for i in range(1, n+1)]
   if (n, x) == (0, 0):
       break

   cnt = 0
   for i in range(len(num_arr)):
       for j in range(i + 1, len(num_arr)):
           k_flg = False
           for k in range(j + 1, len(num_arr)):
               work = num_arr[i] + num_arr[j] + num_arr[k]
               if x == work:
                   cnt += 1
                   k_flg = True
                   break
   ret += [cnt]
for i in ret:
    print i
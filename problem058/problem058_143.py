ret = []
while True:
   n, x = map(int, raw_input().split())
   num_arr = [i for i in range(1, n+1)]
   if (n, x) == (0, 0):
       break

   cnt = 0
   for i in range(n, 0, -1):
       if x - i <= 2:
           continue
       #print "i : %d" % i
       for j in range(i -1, 0, -1):
          if x-i-j <= 0:
              continue
          #print "j : %d" % j
          for k in range(j - 1, 0 , -1):
              if x-i-j-k < 0:
                  continue
              if x -i-j-k == 0:
                  cnt += 1
                  #print "k : %d" % k
                  break
   ret += [cnt]
for i in ret:
    print i
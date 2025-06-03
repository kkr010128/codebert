S = input()
if S >= 0 and S <= 86400:
   a = S // 3600
   b = S % 3600
   c = b // 60
   d = b % 60
   print "%d:%d:%d" % (a, c, d)
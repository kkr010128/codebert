import datetime
from sys import stdin
h1, m1, h2, m2, k = [int(x) for x in stdin.readline().rstrip().split()]

d1 = datetime.datetime(year=2018, month=1, day=7, hour=h1, minute=m1, second=0, microsecond=0)
d2 = datetime.datetime(year=2018, month=1, day=7, hour=h2, minute=m2, second=0, microsecond=0)

delta = d2 - d1

dt2 = delta.seconds / 60

dt2 -= k

if dt2 < 0 :
	dt2 = 0

print(int(dt2))
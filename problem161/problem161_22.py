import math
import collections
def f(a,b,x):
    return math.floor((a*x)/b) - a*math.floor(x/b)
a,b,n=map(int, input().split())
dd = collections.defaultdict(int)

print(f(a,b,min(b-1,n)))

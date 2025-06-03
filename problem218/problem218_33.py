import sys 
from collections import Counter
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
N = int(readline())
l = read().decode().split()
c = Counter(l)
 
max = c.most_common()[0][1]
ans = [i[0] for i in c.items() if i[1] >= max]
 
print('\n'.join(sorted(ans)))
import math
A = int(input())
B = int(input())
N = int(input())
if A> B:
    print(math.ceil(N/A))
else:
    print(math.ceil(N/B))    
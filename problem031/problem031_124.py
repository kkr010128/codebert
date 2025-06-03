import math

while True:
    n = input()
    if n == 0:
        break
    m = map(float,raw_input().split())
    print "%5f" %(math.sqrt(sum([(m[i]-(sum(m)/len(m)))**2 for i in range(n)])/n))
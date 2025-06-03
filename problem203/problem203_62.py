# ABC158 C - Tax Increase
a,b = map(int,input().split())
import math
c=10000
for i in range(1200):
    if math.floor(i*0.08)==a and math.floor(i*0.10)==b:
        c = min(c,i)
if c==10000:
    print(-1)
    exit()
print(c)   
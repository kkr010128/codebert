import math
import re
import copy

h1,m1,h2,m2,k = map(int,input().split())
w1 = h1*60 + m1
w2 = h2 * 60 + m2
w3 = (w2-w1+24*60)%(24*60)
w3 = w3 - k
print(w3)

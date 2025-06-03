import sys
input = sys.stdin.readline
from collections import *

H1, M1, H2, M2, K = map(int, input().split())
print(60*H2+M2-(60*H1+M1)-K)
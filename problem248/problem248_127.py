import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

S=ns().split()
print(S[1]+S[0])
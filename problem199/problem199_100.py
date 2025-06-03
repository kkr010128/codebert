#template
from sys import setrecursionlimit
setrecursionlimit(10**6)
from collections import Counter
def inputlist(): return [int(i) for i in input().split()]
#template
li = ['hi','hihi','hihihi','hihihihi','hihihihihi']
S = input()
if S in li:
    print("Yes")
else:
    print("No")
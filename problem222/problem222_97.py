from collections import Counter as c
N = int(input())
A = list(input().split())
if c(A).most_common()[0][1] == 1: print("YES")
else: print("NO")
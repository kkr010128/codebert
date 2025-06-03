import itertools
#再帰関数のときのRE予防
import sys
sys.setrecursionlimit(312467) 
N = int(input())
List = []
def dfs(S):
    List.append(S)
    if len(S) < N:
      for i in range(ord("a"), ord(max(S))+2):
        dfs(S+[chr(i)])
    return
dfs(["a"])
for i in List:
  if len(i) == N:
    print("".join(i))
  elif len(i) > N:
    break
import sys
sys.setrecursionlimit(10**8)
def line_to_int(): return int(sys.stdin.readline())
def line_to_each_int(): return map(int, sys.stdin.readline().split())
def line_to_list(): return list(map(int, sys.stdin.readline().split()))
def line_to_list_in_iteration(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
# def dp(init, i, j): return [[init]*i for i2 in range(j)]
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
# from itertools import accumulate #A = [0]+list(accumulate(A))
# import bisect #bisect.bisect_left(B, a), bisect.bisect_right(B,a)

x = line_to_list()
print(x.index(0)+1)
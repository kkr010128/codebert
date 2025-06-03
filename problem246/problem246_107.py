N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
import itertools
nums = list(itertools.permutations(range(1,N+1)))
print(abs(nums.index(P)-nums.index(Q)))

n = int(input())
S = [int(s) for s in input().split()]
q = int(input())
T = [int(s) for s in input().split()]

print(sum([t in S for t in T]))
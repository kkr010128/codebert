import itertools
n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

N = [i for i in range(1,n+1)]

N_dict = {v:(i+1) for i,v in enumerate(itertools.permutations(N, n))}
#print(N_dict)

print(abs(N_dict[P] - N_dict[Q]))
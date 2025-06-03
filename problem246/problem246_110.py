from itertools import permutations
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
Z_list = [n for n in range(1, N + 1)]
for i,j in enumerate(permutations(Z_list, r = N)):
    if j == P:
        a = i 
    if j == Q:
        b = i
print(abs(b - a))
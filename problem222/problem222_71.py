N = int(input())
A = [int(s) - 1 for s in input().split()]

M = {}
result = 'YES'
for a in A:
    if a in M.keys():
        result = 'NO'
    M[a] = a

print(result)

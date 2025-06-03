n=int(input())
d = {}
for _ in range(n):
    op,s = input().split()
    if   op == 'insert': d[s] = 'yes'
    elif op == 'find'  : print(d.get(s,'no'))
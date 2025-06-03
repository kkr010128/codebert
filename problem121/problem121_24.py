N = int(input())
letters = 'zabcdefghijklmnopqrstuvwxy'

def solve(N):
    md = N%26
    l = letters[md]
    if md==0: md=26
    if N>26:
        return solve((N-md)//26) + l
    else:
        return l

print(solve(N))

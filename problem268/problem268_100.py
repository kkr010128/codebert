
N = int(input())
A = list(map(int, input().split()))

L = 1000000007

state = [0,0,0]

M = [0,0,0]
for a in A:
    t = None
    n = 0
    for i,s in enumerate(state):
        if s == a:
            t = i
            n += 1
    if n == 0:
        break
    M[n-1] += 1
    state[t] += 1

if n > 0:
    x = 2**30 % L
    y = 3**19 % L


    k = M[1] % x
    l = M[2] % y
    r = 2**k * 3**l % L
    print(r)
else:
    print(0)

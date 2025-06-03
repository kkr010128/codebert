import itertools
n = int(input())
a = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
for _ in range(n):
    b, f, r, v = map(int, input().split())
    a[b-1][f-1][r-1] += v
for b in range(4):
    for f in range(3):
        for r in range(10):
            print('', a[b][f][r], end="")
        print() 
    if b < 3:
        print("#"*20)
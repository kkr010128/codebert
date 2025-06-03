c = { 
    'S' : [0 for _ in range(13)], 'H' : [0 for _ in range(13)],
    'C' : [0 for _ in range(13)], 'D' : [0 for _ in range(13)]
}
 
x = int(input())
for _ in range(x):
    (a, b) = input().split()
    b = int(b)
    c[a][b - 1] = b
 
for a in ('S', 'H', 'C', 'D'):
    for b in range(13):
        if c[a][b] == 0:
            print('{0:s} {1:d}'.format(a, b+1))
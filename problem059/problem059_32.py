import sys

r, c = map(int, raw_input().split())
table = {}

for i in range(r):
    a = map(int, raw_input().split())
    for j in range(c):
        table[(i,j)] = a[j]

for i in range(r+1):
    for j in range(c+1):
        if(i != r and j != c):
            sys.stdout.write(str(table[(i,j)]))
            sys.stdout.write(' ')
        elif(i != r and j == c):
            print sum(table[(i,l)] for l in range(c))
        elif(i == r and j != c):
            sys.stdout.write(str(sum(table[(k,j)] for k in range(r))))
            sys.stdout.write(' ')
        elif(i == r and j == c):
            total = 0
            for k in range(r):
                for l in range(c):
                    total += table[(k,l)]
            print total
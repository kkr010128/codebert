import sys
X=int(input())
for A in range(800):
    for B in range(-800,A+1):
        if X==A**5-B**5:
            print('{} {}'.format(A,B))
            sys.exit()
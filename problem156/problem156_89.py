import sys
X = int(input())
#%%

for a in range(1000):
    for b in range(-1000, 1000):
        if pow(a, 5) - pow(b, 5) == X:
            print(a,b)
            sys.exit( )
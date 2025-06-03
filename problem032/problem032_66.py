import itertools
n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
Z = list(itertools.product(X,Y))
Z = Z[::len(X)+1]
def fn(p):
    D = 0
    for z in Z:
        D += abs(z[0]-z[1])**p
    else:
        print(D**(1/p))
fn(1)
fn(2)
fn(3)
MA = []
for z in Z:
    MA.append(abs(z[0]-z[1]))
print(max(MA))


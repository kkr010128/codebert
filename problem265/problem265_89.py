import math
def taxminus(X):
    return X/1.08,(X+1)/1.08
N=int(input())
min,max=taxminus(N)
min=math.ceil(min)
if min>=max:
    print(":(")
else:
    print(min)
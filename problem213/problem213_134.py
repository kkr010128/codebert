N = int(input())
X = list(map(int, input().split()))

def cost(p):
    res = 0
    for x in X:
        res += (x - p)**2
    return res

m = sum(X) // N
print(min(cost(m), cost(m+1)))
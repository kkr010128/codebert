def minkovsky(A,B,n = 0):
    C = [abs(a - b) for a , b in zip(A,B)]
    if n == 0:
        return max(C)
    else:
        d = 0
        for c in C:
            d += c ** n
        d = d ** (1 / n)
        return d
            
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(minkovsky(A,B,1))
print(minkovsky(A,B,2))
print(minkovsky(A,B,3))
print(minkovsky(A,B))

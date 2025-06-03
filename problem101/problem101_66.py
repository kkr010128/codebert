a, b, c = map(int, input().split())
k = int(input())

def count(v1, v2, k):
    while v1 <= v2 and k >= 0:
        v1 *= 2
        k -= 1
    b = v1
    return v1, v2, k

b, _, k = count(b, a, k)
_, _, k = count(c, b, k)
        
if k < 0:
    print('No')
else:
    print('Yes')

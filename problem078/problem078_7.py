tmp = 10 ** 9 + 7

def div(n,T):
    _ = 1
    for t in range(T):
        _ *= n
        _ %= tmp
    return _
    
N = int(input())
a = div(10,N)
b = div(9,N)
c = div(8,N)

print((a + c - 2 * b) % tmp)
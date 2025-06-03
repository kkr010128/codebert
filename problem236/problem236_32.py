H = int(input())
W = int(input())
N = int(input())

def ceil_div(a, b):
    return (a + b - 1) // b

print(ceil_div(N, max(H, W)))
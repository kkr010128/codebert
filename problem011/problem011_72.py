a, b = map(int, input().split())

def gcd(a, b):
    if a == b:
        return a
    big = max(a, b)
    small = min(a, b)
    while not big % small == 0:
        big, small = small, big%small
    return small
    
print(gcd(a, b))


# 2020/08/08
# AtCoder Beginner Contest 174 - A

# Input
n, a, b = map(int,input().split())

# Calc
sa = abs(b - a)

if sa % 2 == 0:
    ans = sa // 2
else:
    # B go Right and 1 lose
    bgr = n - b + 1
    bgra = a + bgr
    rans = (n - bgra) // 2 + bgr
    
    # A go Left and 1 lose
    agl = a - 1 + 1
    aglb = b - agl
    lans = (aglb - 1) // 2 + agl
    ans = min(rans, lans)

# Output
print(ans)

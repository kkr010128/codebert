a, b, c, d = map(int, input().split())

def kaisuu(atk, hp):
    if (hp/atk) > (hp//atk):
        return hp//atk + 1
    else:
        return hp//atk

if kaisuu(b,c) <= kaisuu(d,a):
    print("Yes")
else:
    print("No")
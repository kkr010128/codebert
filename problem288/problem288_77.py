import math

N = int(input())
even = False

if N % 2 == 0:
    even = True

factor1 = int(math.floor(N ** (1/2)))

# if even:  # Nが偶数の時はfactor1を偶数にしておく
#     if factor1 % 2 == 1:
#         factor1 -= 1
# else:
#     if factor1 % 2 == 0:
#         factor1 -= 1

while True:
    if N % factor1 == 0:
        factor2 = int(N / factor1)
        break
    else:
        factor1 -= 1

print(factor1 + factor2 - 2)

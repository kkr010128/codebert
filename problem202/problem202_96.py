N, A, B = list(map(int, input().split()))

try:
    blue_num = A * (N // (A + B))
    residue = N - ((A + B) * (N // (A + B)))
    if(residue > A):
        blue_num += A
    else:
        blue_num += residue
except ZeroDivisionError:
    blue_num = 0

print(blue_num)
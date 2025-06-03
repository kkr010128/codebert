n = int(input())
a = [int(an) for an in input().split()]

xor_all = 0
for an in a:
    xor_all = xor_all ^ an

anss = [str(xor_all ^ an) for an in a]
print(" ".join(anss))
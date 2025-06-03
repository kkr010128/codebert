st = input().split()
S = st[0]
T = st[1]

ab = input().split()
A = int(ab[0])
B = int(ab[1])
U = input()

new_a = A - 1 if S == U else A
new_b = B-1 if T == U else B

print("{} {}".format(new_a, new_b))

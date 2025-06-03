ri = lambda S: [int(v) for v in S.split()]
N, A, B = ri(input())

q, r = divmod(N, A+B)

blue = (A * q) + r if r <= A else (A * q) + A
print(blue)
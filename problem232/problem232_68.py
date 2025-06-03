[a, b] = [str(i) for i in input().split()]
A = a*int(b)
B = b*int(a)
s = [A, B]
S = sorted(s)
print(S[0])
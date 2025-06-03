Ss, Ts = input().split()
A, B = map(int, input().split())
Us = input().rstrip()

if Ss == Us:
    A -= 1
elif Ts == Us:
    B -= 1

print(A, B)

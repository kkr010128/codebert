line = input()

N, X, T = (int(x) for x in line.split(" "))

print((N + X - 1) // X * T)
a = input()
b, c, d = [int(x) for x in a.split()]
x = [x for x in range(b, c + 1) if x % d == 0]
print(len(x))
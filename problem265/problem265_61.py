n = int(input())

p2 = (n + 1) / 1.08
p1 = n / 1.08
if p2 > int(p2) >= p1:
    print(int(p2))
else:
    print(":(")
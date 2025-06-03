input = input()
L, R, d = [int(n) for n in input.split()]
count = 0
for n in range(L, R+1):
    if n % d == 0:
        count += 1

print(count)
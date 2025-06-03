s = input()
s = s.split()
n = []

for i in s:
    n.append(int(i))

print(n[0] * n[1],end = " ")
print(2 * n[0] + 2 * n[1])

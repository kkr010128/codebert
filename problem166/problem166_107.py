s = input()
t = len(s)

x = []
y = 0

while 10 ** y % 2019 not in x:
    x.append(10 ** y % 2019)
    y += 1

z = len(x)

m = [0 for i in range(2019)]
m[0] = 1
a = 0
for i in reversed(range(0, t)):
    a += x[(t-i-1) % z] * (int(s[i]) % 2019)
    a = a % 2019
    m[a] += 1

def triangle(n):
    if n > 1:
        return n * (n-1) // 2
    else:
        return 0

p = list(map(triangle, m))
# print(p)
print(sum(p))

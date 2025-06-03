s = input()
t = input()

a = []

for i in range(len(s) - len(t) + 1):
    w = s[i:i + len(t)]
    sum = 0
    for j in range(len(t)):
        if w[j] != t[j]:
            sum += 1
    a.append(sum)

print(min(a))

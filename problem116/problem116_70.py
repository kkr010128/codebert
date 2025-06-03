s = input()
t = input()

x = len(s)

num = 0
for i in range(0, x):
    if s[i] != t[i]:
        num += 1

print(num)
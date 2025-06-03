n = input()
p = input()
s = len(n)
count = 0
for i in range(s):
    if n[i] != p[i]:
        count += 1
print(count)
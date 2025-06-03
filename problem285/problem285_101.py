s = open(0).read()

a = [0]
streak = 0
# mx = 0
for c in s:
    if c == '<':
        streak += 1
#         mx = max(mx, streak)
    else:
        streak = 0
    a.append(streak)
#     a.append(mx)

b = [0]
streak = 0
# mx = 0
for c in s[::-1]:
    if c == '>':
        streak += 1
#         mx = max(mx, streak)
    else:
        streak = 0
#     b.append(mx)
    b.append(streak)
b = b[::-1]

print(sum([max(x, y)for x, y in zip(a, b)]))
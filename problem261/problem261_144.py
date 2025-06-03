S = input()
count = 0
for a, b in zip(S, reversed(S)):
    if a != b:
        count += 1
print(count // 2)

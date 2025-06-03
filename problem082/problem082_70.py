s = input()
t = input()


max = 0
for i in range(len(s) -len(t) + 1):
    target = s[i:i+len(t)]
    matched = 0
    for j in range(len(target)):
        if target[j] == t[j]:
            matched += 1
    if matched > max:
        max = matched

print(len(t) - max)

s = input()
t = input()
change = len(t)
for x in range(len(s) - len(t) + 1):
    temp_change = 0
    for y in range(len(t)):
        if s[x+y] != t[y]:
            temp_change += 1
    if change > temp_change:
        change = temp_change
print(change)

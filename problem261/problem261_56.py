s = str(input())
count = 0
for i, j in zip(s, s[::-1]):
    if i != j:
        count += 1
    else:
        pass
print(count//2)
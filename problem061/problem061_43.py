I = input()

for i in range(len(I)):
    if 'a' <= I[i] <= 'z':
        print(I[i].upper(), end = '')
        continue
    if 'A' <= I[i] <= 'Z':
        print(I[i].lower(), end = '')
        continue
    print(I[i], end = '')
print()
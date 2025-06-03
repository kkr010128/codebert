N=input()
total=0
for i in N:
    total += int(i)
print('Yes' if total % 9 == 0 else 'No')
n = int(input())
s = []
for i in range(1, n+1):
    if i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        s.append(i)
print(sum(s))
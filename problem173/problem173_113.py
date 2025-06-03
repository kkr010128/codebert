n = int(input())
a = []
for i in range(1, n+1):
    if i%3 == 0 or i%5 == 0:
        continue
    else:
        a.append(i)
print(sum(a))
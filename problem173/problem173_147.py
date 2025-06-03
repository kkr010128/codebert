N = int(input())

l = []
for i in range(N+1):
    if i % 5 == 0 or i % 3 == 0:
        l.append(0)
    else:
        l.append(i)

print(sum(l))
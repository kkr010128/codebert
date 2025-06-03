input()
l = [int(i) for i in input().split()]
input()
c = 0
for i in input().split():
    for j in l:
        if int(i) == j:
            c += 1
            break
print(c)

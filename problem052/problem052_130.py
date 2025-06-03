n = input()
n = int(n)
l = []

for i in range(1, n+1):
    if i % 3 == 0:
        l.append(i)
    else:
        j = i
        while j > 0:
            if j % 10 == 3:
                l.append(i)
                break
            else:
                j //= 10

for p in l:
    print(" " + str(p), end="")
print()
     

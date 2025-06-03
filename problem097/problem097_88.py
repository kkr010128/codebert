K = int(input())

i = 7 % K

result = set()
for x in range(K):
    if i == 0:
        print(x + 1)
        exit()
    if i in result:
        print(-1)
        exit()
    else:
        result.add(i)

    i = (i * 10 + 7) % K

print(-1)

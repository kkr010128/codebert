x = int(input())
prlist = []
n = 2
sosuu = 0
answer = 0
while n**2 < x:
    for i in prlist:
        if n % i == 0:
            sosuu = 1
            break
    if sosuu == 0:
        prlist.append(n)
    sosuu = 0
    n += 1
sosuu = 1
while answer == 0:
    for j in prlist:
        if x % j == 0:
            sosuu = 2
            break
    if sosuu == 1:
        answer = x
    sosuu = 1
    x += 1
print(answer)
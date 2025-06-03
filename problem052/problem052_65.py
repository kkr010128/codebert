n = int(input())
L = []

for x in range(3,n+1):
    if x % 3 == 0:
        L.append(x)
    else:
        i = x
        while i != 0:
            if i % 10 == 3:
                L.append(x)
                break
            else : i /= 10

print "",

while L != []:
    print L.pop(0),
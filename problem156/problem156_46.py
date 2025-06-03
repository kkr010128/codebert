X = int(input())
flag = False

for A in range(-120, 120):
    for B in range(-120, 120):
        if A**5 - B**5 == X:
            flag = True
            break
    if flag:
        break

print(A, B)

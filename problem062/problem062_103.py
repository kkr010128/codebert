Nsum = 0

while True:
    I = input()
    if int(I) == 0:
        break
    for i in I:
        Nsum += int(i)
    print(Nsum)
    Nsum = 0
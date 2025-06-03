count = 0
W = input().lower()
T = [0]
while True:
    try:
        if T[0] == "END_OF_TEXT":
            break
        for t in T:
            if W == t:
                count += 1
        T = [x.lower() for x in input().split()]
    except EOFError:
        break
    except IndexError:
        break
print(count)
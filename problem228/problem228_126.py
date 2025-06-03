def kougeki(H):
    if H == 1:
        return 1
    else:
        return 2 * kougeki(H//2) + 1

H = int(input())

print(kougeki(H))
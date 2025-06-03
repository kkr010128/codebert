n = int(input())
T = H = 0
for x in range(n):
    t, h = input().split()
    tl = list(t)
    hl = list(h)
    z = min([int(len(tl)),int(len(hl))])
    for k in range(z):
        if ord(tl[k]) > ord(hl[k]):
            T += 3
            break
        elif ord(tl[k]) == ord(hl[k]):
            pass
        else:
            H += 3
            break
    else:
        if len(hl) == len(tl):
            T += 1
            H += 1
        elif z == len(tl):
            H += 3
        else:
            T += 3
print(f"{str(T)} {str(H)}")




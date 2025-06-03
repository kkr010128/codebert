h = int(input())

def rc(h):
    if h == 1:
        return 1
    t = rc(h//2)*2
    return t + 1

print(rc(h))
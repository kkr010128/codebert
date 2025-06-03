a, b, c = map(int, input().split())
def black (a,b,c):
    if a+b+c >= 22:
        return "bust"
    else:
        return "win"
print(black(a,b,c))
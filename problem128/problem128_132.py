x, n = map(int, input().split())
p = list(map(int, input().split()))

def calc(a):
    return abs(a - x)

if not n:
    print(x)
    exit()

l = [i for i in range(102) if i not in set(p)]
print(min(l, key=calc))
